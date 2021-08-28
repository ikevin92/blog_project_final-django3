from categories.api.permissions import isAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet
from categories.api.serializers import CategorySerializer
from categories.models import Category
from django_filters.rest_framework import DjangoFilterBackend, filterset


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [isAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'  # se reemplaza por el id (urlParam)
    # filtros (queryParams)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']

