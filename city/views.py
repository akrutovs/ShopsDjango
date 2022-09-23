from django.shortcuts import render
from .models import City


# Create your views here.
def index(request):
    return render(request, 'city/index.html', {'title': 'Главная страница'})


def show_city(request):
    cities = City.objects.all()
    return render(request, 'city/city.html', {'title': 'Список городов', 'cities': cities})
