from rest_framework import serializers

from airbnb.apps.location.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'room', 'country',
                  'description', 'city', 'created_at']
