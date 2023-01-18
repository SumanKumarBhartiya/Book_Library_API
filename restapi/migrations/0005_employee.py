# Generated by Django 3.0.5 on 2022-12-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_auto_20221215_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.PositiveIntegerField()),
                ('empname', models.CharField(max_length=50)),
                ('empsalary', models.PositiveIntegerField()),
            ],
        ),
    ]
