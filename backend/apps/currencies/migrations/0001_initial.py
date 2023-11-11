# Generated by Django 4.2.7 on 2023-11-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseCurrency', models.CharField(max_length=3)),
                ('currency', models.CharField(max_length=3)),
                ('saleRateNB', models.DecimalField(decimal_places=7, max_digits=10)),
                ('purchaseRateNB', models.DecimalField(decimal_places=7, max_digits=10)),
                ('saleRate', models.DecimalField(decimal_places=7, max_digits=10)),
                ('purchaseRate', models.DecimalField(decimal_places=7, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'currencies',
            },
        ),
    ]