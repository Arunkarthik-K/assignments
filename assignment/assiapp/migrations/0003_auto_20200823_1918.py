# Generated by Django 3.0.6 on 2020-08-23 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assiapp', '0002_auto_20200823_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='Date_of_Sub',
            field=models.DateField(default=datetime.datetime(2020, 8, 23, 19, 18, 38, 952118)),
        ),
    ]
