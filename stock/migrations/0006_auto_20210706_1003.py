# Generated by Django 3.1 on 2021-07-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210706_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ppmu',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stock',
            name='unit',
            field=models.CharField(max_length=20),
        ),
    ]
