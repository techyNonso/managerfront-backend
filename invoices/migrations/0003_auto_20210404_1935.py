# Generated by Django 3.1 on 2021-04-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20210403_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='balance',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='net_price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paid',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.CharField(max_length=20),
        ),
    ]
