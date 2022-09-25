from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from .models import Shop
from .serializers import ShopSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .utils import ShopFilter


# Create your views here.
class ShopViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    # filter_fields = ['id']
    filterset_class = ShopFilter
