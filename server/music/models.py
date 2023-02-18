from django.db import models
from .mixins import\
    UUIDModel, TimeStampModel, SoftDeletionModel


class MusicianPerformer(UUIDModel, TimeStampModel, SoftDeletionModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
