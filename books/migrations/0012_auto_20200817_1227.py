# Generated by Django 2.2.14 on 2020-08-17 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_author_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='title',
        ),
        migrations.AddField(
            model_name='author',
            name='title',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
            preserve_default=False,
        ),
    ]
