# Generated by Django 2.1.2 on 2018-10-11 21:32

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20181010_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='resellers',
            name='zipcode',
            field=models.CharField(default=1, max_length=5, validators=[django.core.validators.RegexValidator(message='Zipcode must be five digits.', regex='^\\d{5}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 11, 14, 32, 28, 992751)),
        ),
    ]
