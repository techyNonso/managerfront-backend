# Generated by Django 3.1 on 2020-08-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20200824_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='branchId',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='companyId',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
