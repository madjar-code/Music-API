from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import\
    ListAPIView, CreateAPIView,\
    RetrieveDestroyAPIView
from rest_framework.parsers import\
    FormParser, JSONParser
from music.models import *
from .serailizers import *


class MPListView(ListAPIView):
    """Getting all musician performers"""
    serializer_class = SimpleMPSerializer
    queryset = MusicianPerformer.active_objects.all()


class AlbumListView(ListAPIView):
    """Getting all albums"""
    serializer_class = SimpleAlbumSerializer
    queryset = Album.active_objects.all()


class SongListView(ListAPIView):
    """Getting all songs"""
    serializer_class = SimpleSongSerializer
    queryset = Song.active_objects.all()


class AlbumDetailView(RetrieveDestroyAPIView):
    """
    Getting detail (and deletion) info about album:
    1) author (musician performe);
    2) songs (names and positions);
    3) and other
    """
    serializer_class = AlbumSerializer
    queryset = Album.active_objects.all()
    lookup_field = 'id'


class MPDetailView(RetrieveDestroyAPIView):
    """
    Getting detail (and deletion) info about musician performer:
    1) name of musician performer;
    2) albums;
    3) and other
    """
    serializer_class = MPSerializer
    queryset = MusicianPerformer.active_objects.all()
    lookup_field = 'id'


class CreateMPView(CreateAPIView):
    """View to create a musician performer"""
    serializer_class = CreateMPSerializer


class CreateAlbumView(CreateAPIView):
    """View to create a album"""
    serializer_class = CreateAlbumSerializer


class CreateSongView(CreateAPIView):
    """View to create a song"""
    serializer_class = CreateSongSerializer


class CreateAlbumSongView(CreateAPIView):
    """View to create the position of a song in an album"""
    serializer_class = CreateAlbumSongSerializer
