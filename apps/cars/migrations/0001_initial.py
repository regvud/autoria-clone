# Generated by Django 4.2.7 on 2023-11-10 11:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\d]{1,20}$', 'Brand first letter must be uppercase,  min 2 max 30 characters')])),
                ('model', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\d]{1,20}$', 'Model first letter must be uppercase,  min 2 max 30 characters')])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2023)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(999999999)])),
                ('currency', models.CharField(choices=[('USD', 'Usd'), ('UAH', 'Uah'), ('EUR', 'Eur')], max_length=3)),
                ('body', models.CharField(choices=[('Jeep', 'Jeep'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('SUV', 'Suv'), ('Coupe', 'Coupe'), ('Van', 'Van'), ('Minivan', 'Minivan'), ('Convertible', 'Convertible'), ('Roadster', 'Roadster'), ('Muscle car', 'Muscle Car')], max_length=11)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
