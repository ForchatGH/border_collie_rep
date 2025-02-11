from django.contrib import admin
from .models import Song, Author, Genre, Album

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'release_year', 'album', 'added']
    list_filter = ['genres', 'author']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'lyrics']
    raw_id_fields = ['author', 'album']
    date_hierarchy = 'added'
    ordering = ['-added']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'release_year']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    raw_id_fields = ['author']
    ordering = ['author']