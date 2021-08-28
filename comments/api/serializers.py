from comments.models import Comment
from rest_framework import fields, serializers
# serializers
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # post = PostSerializer()

    class Meta:
        model = Comment
        fields = ['id',
                  'content',
                  'created_at',
                  'user',
                  'post', ]
