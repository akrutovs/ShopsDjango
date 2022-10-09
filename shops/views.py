from datetime import datetime
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Shop
from .serializers import ShopSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .utils import add_shop
from .filters import ShopFilter

# Create your views here.
class ShopViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShopFilter

    def post(self, request):
        try:
            city_name = request.data['city']
            street_name = request.data['street']
            shop_name = request.data['name']
            start_time = request.data['start_time']
            end_time = request.data['end_time']
            shop_id = add_shop(city_name=city_name, street_name=street_name, shop_name=shop_name, start_time=start_time,
                               end_time=end_time)
            return Response({'id': shop_id}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def show_shop(request):
    s = Shop.objects.all()
    open_field = []
    shops = {}
    time_now = datetime.now().time()
    for el in s:
        if time_now >= el.start_time and time_now<el.end_time:
            open_status = 1
        else:
            open_status = 0
        shops[el] = open_status
        open_field.append(open_status)


    return render(request, 'shop/shop.html', {'title': 'Cписок магазинов', 'shops': shops})