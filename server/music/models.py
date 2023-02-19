from django.db import models
from .mixins import\
    UUIDModel, TimeStampModel, SoftDeletionModel


class MusicianPerformer(UUIDModel, TimeStampModel, SoftDeletionModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Album(UUIDModel, TimeStampModel, SoftDeletionModel):
    name = models.CharField(max_length=255)
    year_of_issue = models.PositiveIntegerField()
    musician_performer = models.ForeignKey(
        to=MusicianPerformer,
        related_name='albums',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'{self.name} - {self.year_of_issue} - {self.musician_performer}'


class Song(UUIDModel, TimeStampModel, SoftDeletionModel):
    name = models.CharField(max_length=255)
    position = models.PositiveIntegerField()
    album = models.ForeignKey(
        to=Album, related_name='songs',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.name} - {self.album.musician_performer}'
