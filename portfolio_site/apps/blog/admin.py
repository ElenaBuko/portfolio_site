from django.contrib import admin
from apps.blog.models import Post, Tag


# @admin.register(Post)
from portfolio_site.admin import PortfolioModelAdmin, portfolio_admin_site


class PostAdmin(PortfolioModelAdmin):

    list_display = ('edit_link', 'title', 'content', 'created')
    list_filter = ('title', 'content')
    list_select_related = ('author', )
    ordering = ('created', )
    search_fields = ('title', 'content')

    class Meta:
        model = Post


# @admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('edit_link', 'value')

    class Meta:
        model = Tag


portfolio_admin_site.register(Post, PostAdmin)
# portfolio_admin_site.register(Tag, TagAdmin)
# portfolio_admin_site.register(Like, LikeAdmin)
