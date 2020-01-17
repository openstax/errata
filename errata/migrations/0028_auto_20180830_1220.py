# Generated by Django 2.0.2 on 2018-08-30 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0027_errata_number_of_errors'),
    ]

    operations = [
        migrations.AddField(
            model_name='errata',
            name='openstax_book',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='errata',
            name='submitted_by_account_id',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
