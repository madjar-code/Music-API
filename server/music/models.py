from django.db import models
from django.core.exceptions import ValidationError
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


class Position(UUIDModel, TimeStampModel, SoftDeletionModel):
    """
    Model describing the position of some song in some album
    """
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    song = models.ForeignKey(to='Song', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.song} - {self.album} - {self.position}'

    @classmethod
    def check_uniqueness(cls, album, song) -> bool:
        all_positions = Position.active_objects.all()
        if all_positions.filter(album=album, song=song).exists():
            return False
        return True

    def clean(self) -> None:
        if not Position.check_uniqueness(self.album, self.song):
            raise ValidationError('This song is already in this album')


class Song(UUIDModel, TimeStampModel, SoftDeletionModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'
