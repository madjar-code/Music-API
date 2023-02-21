from datetime import datetime
from rest_framework import serializers
from rest_framework.serializers import\
    ValidationError, ModelSerializer, SerializerMethodField
from music.models import\
    MusicianPerformer, Album, Song, AlbumSong


class SimpleMPSerializer(ModelSerializer):
    class Meta:
        model = MusicianPerformer
        fields = (
            'id',
            'name',
        )


class SimpleAlbumSerializer(ModelSerializer):
    musician_performer = SimpleMPSerializer()
    class Meta:
        model = Album
        fields = (
            'id',
            'name',
            'year_of_issue',
            'musician_performer',
        )


class SimpleSongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'id',
            'name',
        )


class MPSerializer(ModelSerializer):
    albums = SimpleAlbumSerializer(many=True)

    class Meta:
        model = MusicianPerformer
        fields = (
            'id',
            'name',
            'albums'
        )


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'id',
            'name',
        )


class AlbumSongSerializer(ModelSerializer):
    id = SerializerMethodField()
    name = SerializerMethodField()

    def get_id(self, obj) -> str:
        return obj.song.id

    def get_name(self, obj) -> str:
        return obj.song.name

    class Meta:
        model = AlbumSong
        fields = ('id', 'name', 'position')


class AlbumSerializer(ModelSerializer):
    songs = AlbumSongSerializer(source='albumsong_set', many=True)
    musician_performer = SimpleMPSerializer()
    class Meta:
        model = Album
        fields = (
            'id',
            'name',
            'year_of_issue',
            'songs',
            'musician_performer',
        )

class CreateMPSerializer(ModelSerializer):
    class Meta:
        model = MusicianPerformer
        fields = (
            'id',
            'name',
        )

class CreateAlbumSerializer(ModelSerializer):
    year_of_issue = serializers.IntegerField()

    def validate_year_of_issue(self, value):
        current_date = datetime.now()
        if value < 1000:
            raise ValidationError('Year too small')
        elif value > current_date.year:
            raise ValidationError('The album is not out yet')
        return value

    class Meta:
        model = Album
        fields = (
            'id',
            'name',
            'year_of_issue',
            'musician_performer'
        )


class CreateSongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'id',
            'name'
        )

class CreateAlbumSongSerializer(ModelSerializer):
    position = serializers.IntegerField()

    def validate_position(self, value):
        if value < 1:
            raise ValidationError('This field cannot be less than 0')
        elif value > 100:
            raise ValidationError('This field cannot be less than 100')
        return value

    class Meta:
        model = AlbumSong
        fields = (
            'album',
            'song',
            'position',
        )