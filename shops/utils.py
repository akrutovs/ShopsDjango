import re
from django_filters import rest_framework as filters
from .models import Shop
from city.models import City
from street.models import Street
from datetime import datetime


def get_hour_and_minutes_now():
    current_datetime = datetime.now()
    hour_now = current_datetime.hour
    minutes_now = current_datetime.minute
    return [hour_now, minutes_now]


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


def add_shop(city_name, street_name, shop_name, start_time, end_time):
    if City.objects.filter(name=city_name).exists():  # есть город
        city = City.objects.get(name=city_name)
        city_id = city.id
        if Street.objects.filter(name=street_name).exists():  # в городе есть такая улица
            street = Street.objects.get(name=street_name)
            if city_id == street.city_id:
                street_id = street.id
            else:
                street = Street.objects.create(name=street_name,
                                               city=city)  # новая улица  если страя относится к другому
                street_id = street.id
        else:
            street = Street.objects.create(name=street_name,
                                           city=city)  # новая улица  если страя относится к другому
            street_id = street.id
    else:
        city = City.objects.create(name=city_name)
        city_id = city.id
        street = Street.objects.create(name=street_name, city=city)
        street_id = street.id

    shop = Shop.objects.create(name=shop_name, city=city, street=street, start_time=start_time,
                               end_time=end_time)
    return shop.id


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShopFilter(filters.FilterSet):
    street = CharFilterInFilter(field_name='street__name', lookup_expr='in')
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')
    # open = filters.CharFilter()
    open = filters.NumberFilter(method='open_filter')

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']

    def open_filter(self, queryset, name, value):
        # shops = []
        # [hour_now, minutes_now] = get_hour_and_minutes_now()
        # for shop in queryset.all():
        #     if check_data(start_time=shop.start_time, end_time=shop.end_time, hour_now=hour_now,
        #                   minutes_now=minutes_now) == value:
        #         shops.append(shop.id)
        #
        # return queryset.filter(pk__in=shops)
        time_now = datetime.now().time()
        if value == 0:
            return queryset.filter(start_time__gt=time_now, end_time__lte=time_now)
        elif value == 1:
            return queryset.filter(start_time__lte=time_now, end_time__gt=time_now)
