# Generated by Django 3.2.16 on 2022-12-20 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0014_alter_issue_book_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AlterField(
            model_name='issue_book',
            name='return_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 1, 19, 13, 37, 24, 413772)),
        ),
    ]
