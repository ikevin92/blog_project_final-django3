from django.db.models import fields
from rest_framework import serializers
from posts.models import Post
# serializers
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # para mostrar toda la informacion de un usuario
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'slug',
            'miniature',
            'created_at',
            'published',
            'user',
            'category',
        ]
