from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from .models import Shop
from .serializers import ShopSerializer


# Create your views here.
class ShopViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


