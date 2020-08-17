# Generated by Django 2.2.14 on 2020-08-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_author_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
