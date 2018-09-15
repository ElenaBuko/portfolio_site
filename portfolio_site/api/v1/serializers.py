from rest_framework import serializers

from apps.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'created', 'is_draft', 'tags')
