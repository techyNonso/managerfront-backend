# Generated by Django 3.1 on 2020-10-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20201014_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='expiryDate',
            field=models.DateField(null=True),
        ),
    ]
