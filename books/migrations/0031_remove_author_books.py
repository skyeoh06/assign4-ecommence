# Generated by Django 2.2.14 on 2020-08-19 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0030_auto_20200819_0733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
    ]
