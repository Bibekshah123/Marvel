from rest_framework.pagination import PageNumberPagination

class SuperheroPagination(PageNumberPagination):
    page_size = 2  # default page size
    page_size_query_param = 'page_size'  # allow client to change size (?page_size=10)
    max_page_size = 50  # prevent abuse
