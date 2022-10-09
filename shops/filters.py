from django_filters import rest_framework as filters
from .models import Shop
from datetime import datetime

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShopFilter(filters.FilterSet):
    street = CharFilterInFilter(field_name='street__name', lookup_expr='in')
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')
    open = filters.NumberFilter(method='open_filter')

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']

    def open_filter(self, queryset, name, value):
        time_now = datetime.now().time()
        if value == 0:
            return queryset.filter(start_time__gt=time_now, end_time__lte=time_now)
        elif value == 1:
            return queryset.filter(start_time__lte=time_now, end_time__gt=time_now)
