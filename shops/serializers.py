from rest_framework import serializers
from .models import Shop
from city.serializers import *
from street.serializers import *
from datetime import datetime
from .utils import check_data


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)
    open = serializers.SerializerMethodField('get_open', read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'

    def get_open(self, value):
        current_datetime = datetime.now()
        hour_now = current_datetime.hour
        minutes_now = current_datetime.minute
        return check_data(value.start_time, value.end_time, hour_now, minutes_now)

