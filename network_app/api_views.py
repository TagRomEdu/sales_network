from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from network_app.models import Product, NetworkLink
from network_app.paginator import ProductPagination, NetworkPagination
from network_app.serializers import (ProductSerializer, NetworkLinkSerializer,
                                     NetworkLinkCreateSerializer)
from network_app.filters import LinkCountryFilter
from network_app.permissions import DebtUpdatePermission


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Product Model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ProductPagination


class NetworkLinkViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Network Link.
    """
    queryset = NetworkLink.objects.all()
    permission_classes = (IsAuthenticated, DebtUpdatePermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LinkCountryFilter
    pagination_class = NetworkPagination

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return NetworkLinkCreateSerializer
        else:
            return NetworkLinkSerializer
