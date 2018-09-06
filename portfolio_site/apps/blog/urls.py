from django.urls import path

from apps.blog.views import ListPostView, CreatePostView, UpdatePostView, DeletePostView, \
    DetailPostView

app_name = 'blog'

urlpatterns = [
    path(r'', ListPostView.as_view(), name='index'),
    path(r'^create$', CreatePostView.as_view(), name='post-create'),
    path(r'^edit/(?P<pk>\d+)/$', UpdatePostView.as_view(), name='post-edit'),
    path(r'^delete/(?P<pk>\d+)/$', DeletePostView.as_view(), name='post-delete'),
    path(r'^(?P<pk>\d+)/$', DetailPostView.as_view(), name='post-detail'),
]