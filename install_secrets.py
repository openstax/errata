import json
import os
import boto3

NAMESPACE = '/{}/errata/server'.format(os.environ.get('secrets_env'))
ssm = boto3.client("ssm")
settings_file = open('erratatool/local.py', 'w+')


def _get_ssm_keys(path, next_token=None):
    aws_params = {
        'Path': path,
        'WithDecryption': True
    }

    if next_token:
        aws_params['NextToken'] = next_token

    keys = ssm.get_parameters_by_path(**aws_params)
    print(keys)
    _process_keys(keys['Parameters'])


def _process_keys(keys):
    for key in keys:
        try:
            value = json.loads(key['Value'])
        except ValueError:
            value = key['Value']
        setting_string = "{}='{}'\n".format(key['Name'].split('/')[-1].upper(), value)
        settings_file.write(setting_string)
        globals()[key['Name'].split('/')[-1]] = value


def load_settings():
    next_token = _get_ssm_keys(NAMESPACE)
    while next_token:
        next_token = _get_ssm_keys(NAMESPACE, next_token)


DEBUG = False
load_settings()
