# Generated by Django 3.2.16 on 2022-12-21 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0021_issue_book_is_penalty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('late_fine', models.PositiveIntegerField()),
                ('damage_fine', models.PositiveIntegerField()),
                ('lost_fine', models.PositiveIntegerField()),
                ('issued_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.issue_book')),
            ],
        ),
    ]
