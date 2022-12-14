from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'street', StreetViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls), name='apiStreet')
]