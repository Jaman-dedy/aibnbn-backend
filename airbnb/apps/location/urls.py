from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'location', views.LocationViewSet, basename='location')
urlpatterns = router.urls
