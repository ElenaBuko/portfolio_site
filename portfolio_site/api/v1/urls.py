from django.urls import path

from api.v1.views import PostListView, TagListView, CreateTagView, RetrieveTagView, DestroyTagView, UpdateTagView

from api.v1.views import CreatePostView, RetrievePostView, DestroyPostView, UpdatePostView

app_name = 'v1'

urlpatterns = [
    path(r'posts/', PostListView.as_view(), name='posts_list'),
    path(r'posts/create/', CreatePostView.as_view(), name='posts_create'),
    path(r'posts/<int:pk>/', RetrievePostView.as_view(), name='post_retrieve'),
    path(r'posts/<int:pk>/delete/', DestroyPostView.as_view(), name='post_delete'),
    path(r'posts/<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),

    path(r'tag/', TagListView.as_view(), name='tag_list'),
    path(r'tag/create/', CreateTagView.as_view(), name='tag_create'),
    path(r'tag/<int:pk>/', RetrieveTagView.as_view(), name='tag_retrieve'),
    path(r'tag/<int:pk>/delete/', DestroyTagView.as_view(), name='tag_delete'),
    path(r'tag/<int:pk>/update/', UpdateTagView.as_view(), name='tag_update'),
]
