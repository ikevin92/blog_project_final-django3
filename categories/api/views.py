from categories.api.permissions import isAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet
from categories.api.serializers import CategorySerializer
from categories.models import Category


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [isAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug' # se reemplaza por el id
