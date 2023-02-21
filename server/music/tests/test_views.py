import json
from rest_framework import status
from rest_framework.test import APITestCase
from music.models import *
from music.api.serailizers import *
from server.urls import API_PREFIX


class TestMPViews(APITestCase):
    def setUp(self) -> None:
        self.mp1 =  MusicianPerformer.objects.create(name='Jet')
        self.mp2 =  MusicianPerformer.objects.create(name='The Neighbourhood')
        self.mp3 =  MusicianPerformer.objects.create(name='Royal Blood')
        self.mp2.soft_delete()

    def test_getting_all(self) -> None:
        response = self.client.get(f'/{API_PREFIX}/musician-performers/')
        expected_data = SimpleMPSerializer([self.mp1, self.mp3], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_getting_one_mp(self) -> None:
        response = self.client.get(f'/{API_PREFIX}/musician-performers/{self.mp1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_getting_one_mp_wrong_data(self) -> None:
        response = self.client.get(f'/{API_PREFIX}/musician-performers/qwewe/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mp_creation(self) -> None:
        response = self.client.post(
            f'/{API_PREFIX}/musician-performers/create/',
            data=json.dumps({
                'name': 'New MP'
            }),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_mp_creation_wrong_data(self) -> None:
        response = self.client.post(
            f'/{API_PREFIX}/musician-performers/create/',
            data=json.dumps({
                'name': ''
            }),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestSongViews(APITestCase):
    def setUp(self) -> None:
        self.song1 =  Song.objects.create(name='First Song')
        self.song2 =  Song.objects.create(name='Second Song')
        self.song3 =  Song.objects.create(name='Third Song')
        self.song3.soft_delete()

    def test_getting_all(self) -> None:
        response = self.client.get(f'/{API_PREFIX}/songs/')
        expected_data = SimpleSongSerializer([self.song1, self.song2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_song_creation(self) -> None:
        response = self.client.post(
            f'/{API_PREFIX}/songs/create/',
            data=json.dumps({
                'name': 'New Song'
            }),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_song_creation_wrong_data(self) -> None:
        response = self.client.post(
            f'/{API_PREFIX}/songs/create/',
            data=json.dumps({
                'name': ''
            }),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

