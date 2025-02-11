# Generated by Django 5.1.3 on 2025-01-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_song_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
