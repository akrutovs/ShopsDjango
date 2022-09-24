from rest_framework import serializers

from .models import Shop
from city.serializers import *
from street.serializers import *

class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = StreetSerializer()

    class Meta:
        model = Shop
        fields = '__all__'
