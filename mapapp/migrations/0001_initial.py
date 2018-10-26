# Generated by Django 2.1.2 on 2018-10-26 22:43

import django.core.validators
from django.db import migrations, models
import localflavor.us.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zipcode', localflavor.us.models.USZipCodeField(max_length=10)),
                ('comments', models.TextField(blank=True, max_length=600)),
                ('latitude', models.CharField(max_length=60)),
                ('longitude', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Resellers',
            },
        ),
    ]
