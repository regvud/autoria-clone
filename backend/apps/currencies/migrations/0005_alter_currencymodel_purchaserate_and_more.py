# Generated by Django 4.2.7 on 2023-11-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0004_alter_currencymodel_purchaserate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencymodel',
            name='purchaseRate',
            field=models.DecimalField(decimal_places=7, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='currencymodel',
            name='purchaseRateNB',
            field=models.DecimalField(decimal_places=7, max_digits=20),
        ),
        migrations.AlterField(
            model_name='currencymodel',
            name='saleRate',
            field=models.DecimalField(decimal_places=7, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='currencymodel',
            name='saleRateNB',
            field=models.DecimalField(decimal_places=7, max_digits=20),
        ),
    ]
