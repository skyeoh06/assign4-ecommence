# Generated by Django 2.2.14 on 2020-08-12 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('published', models.DateField()),
                ('ISBN', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('quotes', models.TextField()),
                ('desc', models.TextField()),
                ('cost', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
