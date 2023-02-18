import uuid
from django.db import models
from .managers import SoftDeletionManager


class UUIDModel(models.Model):
    """
    Abstract model for unique ID.
    """
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    
    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    """
    Abstract model with timestamp
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата последнего изменения')

    class Meta:
        abstract = True


class SoftDeletionModel(models.Model):
    """
    Abstract model for soft removal
    """
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active_objects = SoftDeletionManager()

    def soft_delete(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active = True
        self.save()
    
    class Meta:
        abstract=True
