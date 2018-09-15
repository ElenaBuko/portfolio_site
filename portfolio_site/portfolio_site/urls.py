from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from portfolio_site.utils.utils import get_static_urls

urlpatterns = [
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + get_static_urls()
