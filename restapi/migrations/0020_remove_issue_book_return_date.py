# Generated by Django 3.2.16 on 2022-12-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0019_alter_issue_book_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue_book',
            name='return_date',
        ),
    ]