from django.urls import path, include
from .views import *
from rest_framework import routers


class CustomShopRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]


router = routers.DefaultRouter()
router.register(r'shop', ShopViewSet)
# router = CustomShopRouter()
# router.register(r'shop', ShopViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls), name='apiShop'),
    path('shop/',show_shop , name='shop')
]
