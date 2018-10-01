from django.contrib import admin

from apps.custom_auth.forms import UserForm
from apps.custom_auth.models import User
from portfolio_site.admin import PortfolioModelAdmin, portfolio_admin_site


# @admin.register(User)
class UserAdmin(PortfolioModelAdmin):
    list_display = ('edit_link', 'username', 'email', 'role', 'last_login')

    form = UserForm
    model = User

# Register your models here.
portfolio_admin_site.register(User, UserAdmin)

