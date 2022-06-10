from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import LocationManager
from .sirializers import LocationSerializer
from airbnb.utils.http_requests import http_response


class LocationViewSet(viewsets.ViewSet):
    """
    API endpoint that allows fetch location data.
    """
    @action(methods=['get'], detail=False, url_path='*', url_name='location')
    def list_user_activity(self, request):

        user_activity = LocationManager.objects.all().order_by('-created_at')
        serializer = LocationSerializer(user_activity, many=True)

        return http_response(status=status.HTTP_200_OK, data=serializer.data)
