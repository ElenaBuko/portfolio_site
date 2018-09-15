from django.urls import path

from api.v1.views import PostListView

app_name = 'v1'

urlpatterns = [
    path(r'posts/', PostListView.as_view(), name='posts'),
]
