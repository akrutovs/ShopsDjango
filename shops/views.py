from datetime import datetime

from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Shop
from .serializers import ShopSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .utils import ShopFilter, add_shop, check_data


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
    current_datetime = datetime.now()
    hour_now = current_datetime.hour
    minutes_now = current_datetime.minute
    shops = {}
    for el in s:
        shops[el] = check_data(el.start_time, el.end_time, hour_now, minutes_now)
        open_field.append(check_data(el.start_time, el.end_time, hour_now, minutes_now))

    return render(request, 'shop/shop.html', {'title': 'Cписок магазинов', 'shops': shops})
