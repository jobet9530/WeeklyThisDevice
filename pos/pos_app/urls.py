from django.conf.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CustomerViewSet, SaleViewSet, SaleItemViewSet, UserViewSet, frontend

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'saleitems', SaleItemViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('frontend/', frontend, name='frontend'),
    path('product/', frontend, name='product'),
    path('customer/', frontend, name='customer'),
    path('sale/', frontend, name='sale'),
    path('saleitem/', frontend, name='saleitem'),
    path('user/', frontend, name='user')
]

