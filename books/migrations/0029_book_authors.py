# Generated by Django 2.2.14 on 2020-08-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0028_auto_20200819_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]
