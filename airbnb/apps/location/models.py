from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from .managers import LocationManager


class Location(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    room = models.CharField(verbose_name=_(
        "room"), max_length=30, blank=True, null=True)
    country = models.CharField(verbose_name=_(
        "country"), max_length=30, blank=True, null=True)
    city = models.CharField(verbose_name=_(
        "city"), max_length=30, blank=True, null=True)
    description = models.CharField(verbose_name=_(
        "description"), max_length=255, blank=True, null=True,)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("updated at"))
    deleted_at = models.DateTimeField(
        auto_now=False, verbose_name=_("deleted at"), null=True)

    objects = LocationManager()

    class Meta:
        db_table = "user_activity"
        ordering = ("room", "country", "city", "description")
