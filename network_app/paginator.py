from rest_framework import pagination


class NetworkPagination(pagination.PageNumberPagination):
    """
    Custom class for pagination Network Links.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 30


class ProductPagination(pagination.PageNumberPagination):
    """
    Custom class for pagination Products.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 30
