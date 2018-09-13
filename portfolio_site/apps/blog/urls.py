from django.urls import path

from apps.blog.views import ListPostView, CreatePostView, UpdatePostView, DeletePostView, \
    DetailPostView

app_name = 'blog'

urlpatterns = [
    path(r'', ListPostView.as_view(), name='index'),
    path(r'create/', CreatePostView.as_view(), name='post-create'),
    path(r'edit/<int:pk>/', UpdatePostView.as_view(), name='post-edit'),
    path(r'delete/<int:pk>/', DeletePostView.as_view(), name='post-delete'),
    path(r'<int:pk>/', DetailPostView.as_view(), name='post-detail'),
]
