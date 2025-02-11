from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name='songs'

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/<slug:author>/', views.author_detail, name='author_detail'),
    path('authors/<slug:author>/<slug:album>', views.album_detail, name='album_detail'),
    path('genres/<slug:genre>/', views.genre_detail, name='genre_detail'),
    path('<slug:author>/<slug:song>/', views.song_detail, name='song_detail'),
    path('genres/', views.genres_list, name='genres_list'),
    path('authors/', views.authors_list, name='authors_list'),
    path('search/', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)