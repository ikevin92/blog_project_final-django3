from posts.api.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.permissions import isAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [isAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    # urlParams
    lookup_field = 'slug'
    # queryparams
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__id','category__slug']
    # filterser_fields = ['category']
