from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('city/', views.show_city, name='city'),
    path('api/v1/city/',views.CityAPIView.as_view(), name='apiCity')
]
