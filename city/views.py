from django.shortcuts import render
from rest_framework import generics
from .models import City
from .serializers import CitySerializer


class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


# Create your views here.
def index(request):
    return render(request, 'city/index.html', {'title': 'Главная страница'})


def show_city(request):
    cities = City.objects.order_by('id')
    return render(request, 'city/city.html', {'title': 'Список городов', 'cities': cities})
