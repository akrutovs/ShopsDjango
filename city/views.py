from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import City
from .serializers import CitySerializer
from street.models import Street


class CityViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    #список улиц города
    @action(methods=['get'], detail=True)
    def street(self, request, pk=None):
        try:
            streets = Street.objects.filter(city=pk)
            return Response({'streets': [s.name for s in streets]}, status = status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, 'city/index.html', {'title': 'Главная страница'})


def show_city(request):
    cities = City.objects.order_by('id')
    return render(request, 'city/city.html', {'title': 'Список городов', 'cities': cities})
