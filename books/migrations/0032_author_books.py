# Generated by Django 2.2.14 on 2020-08-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0031_remove_author_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
