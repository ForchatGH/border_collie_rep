from django.shortcuts import render, get_object_or_404
from .models import Song, Author, Genre, Album
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def index(request):
    recent_songs = Song.objects.order_by('-added')[:10]
    genres = Genre.objects.order_by('name')[:10]
    authors = Author.objects.order_by('name')[:10]
    albums = Album.objects.order_by('title')[:10]
    return render(request, 'songs/index.html', {
        'recent_songs': recent_songs,
        'genres': genres,
        'authors': authors,
        'albums': albums
    })

def song_detail(request, author, song):
    song = get_object_or_404(Song,
                             slug=song,
                             author__slug=author)
    author = song.author
    return render(request, 'songs/song_detail.html', {'song': song})

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'songs/genres_list.html', {'genres': genres})

def genre_detail(request, genre):
    genre = get_object_or_404(Genre,
                               slug=genre)
    songs = Song.objects.filter(genres__name=genre.name)
    return render(request, 'songs/genre_detail.html', {'genre': genre, 'songs': songs})

def authors_list(request):
    authors = Author.objects.order_by('name')[:10]
    return render(request, 'songs/authors_list.html', {'authors': authors})

def author_detail(request, author):
    author = get_object_or_404(Author,
                               slug=author)
    albums = Album.objects.filter(author=author)
    songs = Song.objects.filter(author=author)
    return render(request, 'songs/author_detail.html', {
        'author': author,
        'albums': albums,
        'songs': songs
    })

def album_detail(request, author, album):
    album = get_object_or_404(Album,
                              slug=album,
                              author__slug=author)
    songs = Song.objects.filter(album=album)
    return render(request, 'songs/album_detail.html', {'album': album, 'songs': songs})

def search(request):
    query = request.GET.get('q')
    if query:
        search_vector = SearchVector('title', 'lyrics')
        search_query = SearchQuery(query)
        results = Song.objects.annotate(
            search=SearchVector('title', 'lyrics'),
            rank=SearchRank(search_vector, search_query)
        ).filter(search=query).order_by('-rank')
    else:
        results = []
    return render(request, 'songs/search_results.html', {'results': results, 'query': query})
