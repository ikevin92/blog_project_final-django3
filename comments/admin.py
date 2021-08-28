from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content',
        'created_at',
        'user',
        'post',
    ]
