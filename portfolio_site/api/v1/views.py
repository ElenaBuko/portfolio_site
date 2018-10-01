from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView)
from rest_framework import permissions

from api.v1.permissions import RoleIsAdministrator, RoleIsAdministratorOrManager
from apps.blog.models import Post, Tag
from api.v1.serializers import PostSerializer, TagSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny, )


class CreatePostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (RoleIsAdministratorOrManager, )


class RetrievePostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

class DestroyPostView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (RoleIsAdministrator, )



class UpdatePostView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (RoleIsAdministratorOrManager, )

################Tag View########################

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CreateTagView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RetrieveTagView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DestroyTagView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UpdateTagView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer