from categories.api.permissions import isAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet
from categories.api.serializers import CategorySerializer
from categories.models import Category


class CategoryApiViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [isAdminOrReadOnly]
