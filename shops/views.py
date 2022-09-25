from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Shop
from city.models import City
from street.models import Street
from .serializers import ShopSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .utils import ShopFilter, add_shop


# Create your views here.
class ShopViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    # filter_fields = ['id']
    filterset_class = ShopFilter

    def post(self, request):
        city_name = request.data['city']
        street_name = request.data['street']
        shop_name = request.data['name']
        start_time = request.data['start_time']
        end_time = request.data['end_time']
        shop_id = add_shop(city_name=city_name, street_name=street_name, shop_name=shop_name, start_time=start_time,
                           end_time=end_time)
        return Response({'id': shop_id})
