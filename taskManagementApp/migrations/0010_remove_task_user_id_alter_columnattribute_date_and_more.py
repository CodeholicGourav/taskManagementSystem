# Generated by Django 4.0.4 on 2022-06-13 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0009_alter_columnattribute_date_alter_comment_date_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 12, 42, 42, 624332)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 12, 42, 42, 625331)),
        ),
    ]
