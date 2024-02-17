from rest_framework.routers import DefaultRouter

from network_app.api_views import NetworkLinkViewSet, ProductViewSet
from network_app.apps import NetworkAppConfig

app_name = NetworkAppConfig.name

router = DefaultRouter()
router.register(r'network', NetworkLinkViewSet, basename='network_link')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    # add your additional urls
] + router.urls
