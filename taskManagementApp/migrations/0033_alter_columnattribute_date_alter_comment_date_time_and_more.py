# Generated by Django 4.0.4 on 2022-06-16 11:11

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0032_alter_columnattribute_date_alter_comment_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 16, 41, 43, 590269)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 16, 41, 43, 591267)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(default=uuid.uuid4, null=True, unique=True),
        ),
    ]