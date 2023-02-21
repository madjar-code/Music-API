from django.test import TestCase
from music.models import *
from music.api.serailizers import *


class TestMPSerializers(TestCase):
    def setUp(self) -> None:
        self.mp1 = MusicianPerformer.objects.create(name="Bush")
        self.mp2 = MusicianPerformer.objects.create(name="Nirvana")
        self.data_to_create1 = {
            'name': 'The Strokes'
        }
        self.data_to_create2 = {
            'name': ''
        }
    
    def test_simple_serializer(self) -> None:
        data = SimpleMPSerializer([self.mp1, self.mp2], many=True).data
        expected_data = [
            {
                'id': str(self.mp1.id),
                'name': self.mp1.name
            },
            {
                'id': str(self.mp2.id),
                'name': self.mp2.name
            }
        ]
        self.assertEqual(expected_data, data)

    def test_detail_serializer(self) -> None:
        data = MPSerializer([self.mp1, self.mp2], many=True).data
        expected_data = [
            {
                'id': str(self.mp1.id),
                'name': self.mp1.name,
                'albums': []
            },
            {
                'id': str(self.mp2.id),
                'name': self.mp2.name,
                'albums': []
            }
        ]
        self.assertEqual(expected_data, data)

    def test_creation_serilaizer(self) -> None:
        serializer1 = CreateMPSerializer(
            data = self.data_to_create1
        )
        serializer2 = CreateMPSerializer(
            data = self.data_to_create2
        )
        self.assertTrue(serializer1.is_valid())
        self.assertFalse(serializer2.is_valid())


class TestAlbumSerializers(TestCase):
    def setUp(self) -> None:
        self.mp1 = MusicianPerformer.objects.create(name="Bush")
        self.mp2 = MusicianPerformer.objects.create(name="Nirvana")
        self.album1 = Album.objects.create(
            name="The Science of Things",
            year_of_issue=1999,
            musician_performer=self.mp1
        )
        self.album2 = Album.objects.create(
            name="Nevermind",
            year_of_issue=1991,
            musician_performer=self.mp2
        )

        self.data_to_create1 = {
            'name': 'Bleach',
            'year_of_issue': 1989,
            'musician_performer': str(self.mp2.id)
        }
        self.data_to_create2 = {
            'name': 'Bleach',
            'year_of_issue': 12,
            'musician_performer': str(self.mp2.id)
        }

        self.data_to_create3 = {
            'name': 'Bleach',
            'year_of_issue': 20000,
            'musician_performer': str(self.mp2.id)
        }

        self.data_to_create4 = {
            'name': 'Bleach',
            'year_of_issue': 2000,
            'musician_performer': str(self.mp2.id)[:-2]
        }


    def test_simple_serializer(self) -> None:
        data = SimpleAlbumSerializer([self.album1, self.album2], many=True).data
        expected_data = [
            {
                'id': str(self.album1.id),
                'name': self.album1.name,
                'year_of_issue': self.album1.year_of_issue,
                'musician_performer': {
                    'id': str(self.album1.musician_performer.id),
                    'name': self.album1.musician_performer.name
                }
            },
            {
                'id': str(self.album2.id),
                'name': self.album2.name,
                'year_of_issue': self.album2.year_of_issue,
                'musician_performer': {
                    'id': str(self.album2.musician_performer.id),
                    'name': self.album2.musician_performer.name
                }
            },
        ]
        self.assertEqual(data, expected_data)

    def test_detail_serializer(self) -> None:
        data = AlbumSerializer(self.album1).data
        expected_data = {
            'id': str(self.album1.id),
            'name': self.album1.name,
            'year_of_issue': self.album1.year_of_issue,
            'songs': [],
            'musician_performer': {
                'id': str(self.album1.musician_performer.id),
                'name': self.album1.musician_performer.name
            }
        }
        self.assertEqual(data, expected_data)

    def test_creation_serializer(self) -> None:
        serializer1 = CreateAlbumSerializer(data = self.data_to_create1)
        serializer2 = CreateAlbumSerializer(data = self.data_to_create2)
        serializer3 = CreateAlbumSerializer(data = self.data_to_create3)
        serializer4 = CreateAlbumSerializer(data = self.data_to_create4)
        self.assertTrue(serializer1.is_valid())
        self.assertFalse(serializer2.is_valid())
        self.assertFalse(serializer3.is_valid())
        self.assertFalse(serializer4.is_valid())


class TestSongSerializers(TestCase):
    def setUp(self) -> None:
        self.song1 = Song.objects.create(name="Bush")
        self.song2 = Song.objects.create(name="Nirvana")
        self.data_to_create1 = {
            'name': 'Last Night'
        }
        self.data_to_create2 = {
            'name': ''
        }
    
    def test_simple_serializer(self) -> None:
        data = SimpleSongSerializer([self.song1, self.song2], many=True).data
        expected_data = [
            {
                'id': str(self.song1.id),
                'name': self.song1.name
            },
            {
                'id': str(self.song2.id),
                'name': self.song2.name
            }
        ]
        self.assertEqual(expected_data, data)

    def test_creation_serilaizer(self) -> None:
        serializer1 = CreateSongSerializer(
            data = self.data_to_create1
        )
        serializer2 = CreateSongSerializer(
            data = self.data_to_create2
        )
        self.assertTrue(serializer1.is_valid())
        self.assertFalse(serializer2.is_valid())


class TestAlbumSongSerializer(TestCase):
    def setUp(self) -> None:
        self.mp1 = MusicianPerformer.objects.create(name="Bush")
        self.album1 = Album.objects.create(
            name="The Science of Things",
            year_of_issue=1999,
            musician_performer=self.mp1
        )
        self.song1 = Song.objects.create(name="Glycerin")

        self.album2 = Album.objects.create(
            name="The Kingdom",
            year_of_issue=2020,
            musician_performer=self.mp1
        )
        self.song2 = Song.objects.create(name="Jesus Online")

        self.albumsong1 = AlbumSong.objects.create(
            album=self.album1,
            song=self.song1,
            position=10
        )

        self.data_to_create1 = {
            'album': str(self.album2.id),
            'song': str(self.song2.id),
            'position': 10
        }
        self.data_to_create2 = {
            'album': self.album2.id,
            'song': 'asifusdf23',
            'position': 1
        }
        self.data_to_create3 = {
            'album': self.album2.id,
            'song': self.song2.id,
            'position': 0,
        }

    def test_serializer(self) -> None:
        data = AlbumSongSerializer(self.albumsong1).data
        expected_data = {
            'id': self.albumsong1.song.id,
            'name': self.albumsong1.song.name,
            'position': self.albumsong1.position
        }
        self.assertEqual(data, expected_data)

    def test_creation_serializer(self) -> None:
        serializer1 = CreateAlbumSongSerializer(data = self.data_to_create1)
        serializer2 = CreateAlbumSongSerializer(data = self.data_to_create2)
        serializer3 = CreateAlbumSongSerializer(data = self.data_to_create3)
        self.assertTrue(serializer1.is_valid())
        self.assertFalse(serializer2.is_valid())
        self.assertFalse(serializer3.is_valid())