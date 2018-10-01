from rest_framework import serializers

from apps.blog.models import Post, Tag


class PostSerializer(serializers.ModelSerializer):
    # likes = PostLikeSerializer(read_only=True)
    # tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created', 'is_draft', 'tags')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'value')
