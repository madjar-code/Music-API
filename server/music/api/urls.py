from django.urls import path
from .views import *

app_name = 'music'

urlpatterns = [
    path('musician-performers/', MPListView.as_view(), name='musician_performers'),
    path('musician-performers/create/', CreateMPView.as_view(), name='musician_performer_creation'),
    path('musician-performers/<str:id>/', MPDetailView.as_view(), name='musician_performer_detail'),
    path('albums/', AlbumListView.as_view(), name='albums'),
    path('albums/create/', CreateAlbumView.as_view(), name='album_creation'),
    path('albums/<str:id>/', AlbumDetailView.as_view(), name='album_detail'),
    path('songs/', SongListView.as_view(), name='songs'),
    path('songs/create/', CreateSongView.as_view(), name='song_creation'),
    path('album-song/', CreateAlbumSongView.as_view(), name='album_song'),
]