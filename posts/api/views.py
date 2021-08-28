from posts.api.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.permissions import isAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [isAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    # urlParams
    lookup_field = 'slug'
