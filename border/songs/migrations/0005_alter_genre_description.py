# Generated by Django 5.1.3 on 2025-01-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_album_slug_genre_slug_song_slug_alter_album_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, unique=True),
        ),
    ]
