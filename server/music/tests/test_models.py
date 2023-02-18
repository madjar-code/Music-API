from uuid import UUID
from django.test import TestCase
from music.models import\
    MusicianPerformer


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
    
    def test_musician_performer_uuid(self) -> None:
        self.assertEqual(type(self.mp.id), UUID)
    
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

    