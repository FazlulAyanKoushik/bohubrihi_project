from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class MypageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10
    # last_page_strings = 'end'
    

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 10
    