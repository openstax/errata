import json
import os
import boto3

# these are set in deployment CFN templates (or can be overridden locally)
NAMESPACE = '/{}/errata/server'.format(os.environ.get('ENV_NAME'))
REGION = os.environ.get('AWS_REGION')

ssm = boto3.client("ssm", region_name=REGION)
settings_file = open('erratatool/local.py', 'w+')


def _get_ssm_keys(path, next_token=None):
    aws_params = {
        'Path': path,
        'WithDecryption': True,
        'Recursive': True
    }

    if next_token:
        aws_params['NextToken'] = next_token

    keys = ssm.get_parameters_by_path(**aws_params)
    _process_keys(keys['Parameters'])


def _process_keys(keys):
    for key in keys:
        try:
            setting_value = json.loads(key['Value'])
        except ValueError:
            setting_value = key['Value']
        
        # build the settings key
        setting_key = key['Name'].replace(NAMESPACE, '')[1:].replace('/', '_').upper()
        
        setting_string = "{}='{}'\n".format(setting_key, setting_value)
        settings_file.write(setting_string)
        globals()[setting_key] = setting_value


def load_settings():
    next_token = _get_ssm_keys(NAMESPACE)
    while next_token:
        next_token = _get_ssm_keys(NAMESPACE, next_token)


DEBUG = False
load_settings()
