# Generated by Django 4.0.4 on 2022-06-15 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0020_alter_columnattribute_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 14, 0, 14, 805107)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 14, 0, 14, 807107)),
        ),
    ]