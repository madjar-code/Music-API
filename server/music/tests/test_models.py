from uuid import UUID
from datetime import datetime
from django.test import TestCase
from music.models import\
    MusicianPerformer, Album, Song


class TestMusicianPerformerModel(TestCase):
    def setUp(self) -> None:
        self.mp = MusicianPerformer.objects.create(
            name='Arctic Monkeys'
        )
        self.mp2 = MusicianPerformer.objects.create(
            name='Kaleo'
        )
    
    def test_musician_performer_can_be_created(self) -> None:
        self.assertEqual(str(self.mp), 'Arctic Monkeys')
    
    def test_soft_deletion(self) -> None:
        self.assertTrue(self.mp.is_active)
        self.mp.soft_delete()
        self.assertFalse(self.mp.is_active)
        self.mp.restore()
        self.assertTrue(self.mp.is_active)
    
    def test_getting_active_mp(self) -> None:
        mp_objects = MusicianPerformer.active_objects.all()
        self.assertTrue(self.mp in mp_objects)
        self.assertTrue(self.mp2 in mp_objects)
        self.mp2.soft_delete()
        new_mp_objects = MusicianPerformer.active_objects.all()
        self.assertFalse(self.mp2 in new_mp_objects)


class TestAlbumModel(TestCase):
    def setUp(self) -> None:
        self.mp = MusicianPerformer.objects.create(
            name='Arctic Monkeys'
        )

        self.album = Album.objects.create(
            name='AM',
            year_of_issue=2012,
            musician_performer = self.mp
        )

    def test_album_can_be_created(self) -> None:
        self.assertEqual(str(self.album), 'AM - 2012 - Arctic Monkeys')

    def test_album_uuid(self) -> None:
        self.assertEqual(type(self.album.id), UUID)


class TestSongModel(TestCase):
    def setUp(self) -> None:
        self.mp = MusicianPerformer.objects.create(
            name='Kaleo'
        )
    
        self.album1 = Album.objects.create(
            name='A/B',
            year_of_issue=2016,
            musician_performer = self.mp
        )
            
        self.album2 = Album.objects.create(
            name='A/B',
            year_of_issue=2016,
            musician_performer = self.mp
        )

        self.song = Song.objects.create(
            name='Automobile',
            position=7,
            album=self.album
        )

    def test_song_can_be_created(self) -> None:
        self.assertEqual(str(self.song), 'Automobile - Kaleo')
    
    def test_timestamp(self) -> None:
        self.assertEqual(type(self.song.created_at), datetime)
        self.assertEqual(type(self.song.updated_at), datetime)
