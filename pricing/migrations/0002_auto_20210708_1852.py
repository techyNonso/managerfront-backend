# Generated by Django 3.1 on 2021-07-08 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricing',
            old_name='charge',
            new_name='branches_allowed',
        ),
    ]
