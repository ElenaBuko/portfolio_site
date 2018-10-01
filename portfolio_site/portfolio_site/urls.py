from django.conf.urls import include
from django.urls import path

from portfolio_site.admin import portfolio_admin_site
from portfolio_site.utils.utils import get_static_urls
# from portfolio_site.views import MainRedirectView

urlpatterns = [
    # path('', MainRedirectView.as_view()),
    path('auth/', include('apps.custom_auth.urls', namespace='auth')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('admin/', portfolio_admin_site.urls),
    path('api/', include('api.urls', namespace='api')),
]
urlpatterns = urlpatterns + get_static_urls()
