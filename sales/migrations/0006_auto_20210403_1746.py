# Generated by Django 3.1 on 2021-04-03 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20200916_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='toPay',
        ),
    ]
