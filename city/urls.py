from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'city', CityViewSet)

urlpatterns = [
    # path('', index, name='home'),
    path('city/', show_city, name='city'),
    path('api/v1/', include(router.urls), name='apiCity'),
    path('city/<int:city_id>/street/', show_city_streets, name='city_streets')
]
