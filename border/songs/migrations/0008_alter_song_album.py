# Generated by Django 5.1.5 on 2025-01-30 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_alter_author_name_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_songs', to='songs.album'),
        ),
    ]
