from django.db import models
from airbnb.resources import error_messages
import datetime
from django.core.exceptions import ValidationError


class LocationManager(models.Manager):
    def create_location(self, **kwargs):
        location = self.model()

        if not kwargs.get('room'):
            raise ValidationError(
                error_messages.REQUIRED.format('Activity room is '))

        if not kwargs.get('description'):
            raise ValidationError(
                error_messages.REQUIRED.format('Activity description is '))

        location.room = kwargs.get('room')
        location.description = kwargs.get('description')

        location.save(using=self._db)
        return location

    def delete(self, id=None, **kwargs):
        location = self.model.objects.get(id=id)

        location.deleted_at = datetime.datetime.now()

        location.save(using=self._db)
        return location
