# Generated by Django 2.2.14 on 2020-08-19 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0027_auto_20200819_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
    ]
