from rest_framework import serializers
from .models import Shop
from city.models import City
from street.models import Street
from city.serializers import *
from street.serializers import *
from datetime import datetime



class ShopSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', queryset=City.objects)
    street = serializers.SlugRelatedField(slug_field='name', queryset=Street.objects)
    open = serializers.SerializerMethodField('get_open', read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'

    def get_open(self, value):
        time_now = datetime.now().time()
        if time_now >= value.start_time and time_now < value.end_time:
            return 1
        else:
            return 0



