from rest_framework.generics import ListAPIView

from apps.blog.models import Post
from api.v1.serializers import PostSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
