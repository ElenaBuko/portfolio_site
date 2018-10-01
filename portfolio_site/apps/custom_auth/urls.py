from django.urls import path

from apps.custom_auth.views import LoginView, LogoutView

app_name = 'custom_auth'

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
]