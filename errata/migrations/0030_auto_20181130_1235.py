# Generated by Django 2.0.2 on 2018-11-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0029_auto_20181002_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errata',
            name='resolution',
            field=models.CharField(blank=True, choices=[('Duplicate', 'Duplicate'), ('Not An Error', 'Not An Error'), ('Will Not Fix', 'Will Not Fix'), ('Approved', 'Approved'), ('Major Book Revision', 'Major Book Revision'), ('Technical Error', 'Technical Error'), ('Sent to Customer Support', 'Sent to Customer Support'), ('More Information Requested', 'More Information Requested')], max_length=100, null=True),
        ),
    ]
