from django.contrib import admin
from django.utils.html import format_html


class PortfolioModelAdmin(admin.ModelAdmin):

    def edit_link(self, obj):
        return format_html('<span>Edit</span>')

    edit_link.sort_desription = ''


class PortfolioAdminSite(admin.AdminSite):
    site_header = 'Porwerwerwetfilio'

portfolio_admin_site = PortfolioAdminSite()