from django.db import models
from django.urls import reverse
from PIL import Image


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='authors/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            img.thumbnail((300, 300))
            img.save(self.image.path)

    class Meta:
        verbose_name = 'автора'
        verbose_name_plural = 'авторы'

    def get_absolute_url(self):
        return reverse('songs:author_detail',
                       args=[self.slug])

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, unique=True)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def get_absolute_url(self):
        return reverse('songs:genre_detail',
                       args=[self.slug])

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='albums/', blank=True, null=True)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='author_albums')
    release_year = models.PositiveIntegerField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', 'author'], name='unique_album_slug_per_author')
        ]
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cover:
            img = Image.open(self.cover.path)
            img.thumbnail((300, 300))
            img.save(self.cover.path)

    def get_absolute_url(self):
        return reverse('songs:album_detail',
                       args=[self.author.slug,
                             self.slug])

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    cover = models.ImageField(upload_to='songs/', blank=True, null=True)
    lyrics = models.TextField()
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='author_songs')
    release_year = models.PositiveIntegerField(blank=True)
    album = models.ForeignKey(Album,
                              on_delete=models.SET_NULL,
                              related_name='album_songs',
                              null=True,
                              blank=True
                              )
    genres = models.ManyToManyField(Genre,
                                    related_name='genre_songs')
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', 'author'], name='unique_song_slug_per_author')
        ]
        verbose_name = 'песню'
        verbose_name_plural = 'песни'

    def get_absolute_url(self):
        return reverse('songs:song_detail',
                       args=[self.author.slug,
                             self.slug])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cover:
            img = Image.open(self.cover.path)
            img.thumbnail((300, 300))
            img.save(self.cover.path)

    def __str__(self):
        return self.title
