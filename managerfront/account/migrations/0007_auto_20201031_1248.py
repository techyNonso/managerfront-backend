# Generated by Django 3.1 on 2020-10-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20201022_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='expiration_limit',
            field=models.IntegerField(default=90),
        ),
        migrations.AlterField(
            model_name='account',
            name='stock_limit',
            field=models.IntegerField(default=10),
        ),
    ]
