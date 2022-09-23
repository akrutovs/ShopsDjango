from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City
from .serializers import CitySerializer


class CityAPIView(APIView):
    def get(self, request):
        lst = City.objects.all()
        return Response({"cities": CitySerializer(lst, many=True).data})

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


# Create your views here.
def index(request):
    return render(request, 'city/index.html', {'title': 'Главная страница'})


def show_city(request):
    cities = City.objects.order_by('id')
    return render(request, 'city/city.html', {'title': 'Список городов', 'cities': cities})
