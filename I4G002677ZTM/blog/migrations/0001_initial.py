# Generated by Django 4.0.6 on 2022-07-31 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=20)),
                ('book_author', models.CharField(max_length=20)),
                ('year_published', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Book Store',
                'verbose_name_plural': 'Book Store',
            },
        ),
    ]
