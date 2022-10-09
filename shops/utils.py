from .models import Shop
from city.models import City
from street.models import Street


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
