# Generated by Django 3.1.1 on 2021-07-23 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210723_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 23, 9, 7, 4, 189623)),
        ),
    ]
