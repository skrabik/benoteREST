from rest_framework import generics, viewsets
from .models import Content
from .serializers import ContentSerializer
from  rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAdminOrReadOnly


class ContentMixin:
    def get_queryset(self):
        queryset = Content.objects.filter()
        return queryset
    serializer_class = ContentSerializer

class ContentAPIPaginatoin(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ContentAPIList(ContentMixin, generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = ContentAPIPaginatoin

class ContentAPIUpdate(ContentMixin, generics.RetrieveUpdateAPIView):
    pass

class ContentAPIDestoroy(ContentMixin, generics.RetrieveDestroyAPIView):
    pass
