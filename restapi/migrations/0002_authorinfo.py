# Generated by Django 3.0.5 on 2022-12-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('author_image', models.ImageField(upload_to='author_image')),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]