import re
from django_filters import rest_framework as filters
from .models import Shop


def get_hour_and_minute(time):
    if len(time) == 4:
        time = '0' + time
    split_time = re.findall(r'^([0-1][0-9]|2[0-3]):([0-5][0-9])$', time)
    minutes = int(split_time[0][1])
    hour = split_time[0][0]
    if hour[0] == '0':
        hour = int(hour[1])
    else:
        hour = int(hour)
    return [hour, minutes]


def check_data(start_time, end_time, hour_now, minutes_now):
    [hour_start, minutes_start] = get_hour_and_minute(start_time)
    [hour_end, minutes_end] = get_hour_and_minute(end_time)
    if (hour_now == hour_start and minutes_now > minutes_start) or (hour_now > hour_start and hour_now < hour_end):
        return 1
    else:
        return 0


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShopFilter(filters.FilterSet):
    name = filters.CharFilter()
    street = CharFilterInFilter(field_name='street__name', lookup_expr='in')
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')
    open = CharFilterInFilter()

    class Meta:
        model = Shop
        fields = ['name', 'city', 'street', 'open']
