from django.db.models import Q
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, TemplateView,
                                  UpdateView)

from apps.blog.mixins import RoleVerificationMixin
from apps.blog.models import Post, Tag
from apps.custom_auth.enums import RoleTypes


class ListPostView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        t = self.request.GET.get('t')
        if q:
            queryset = self.filter_by_title_and_content(queryset, q)
        elif t:
            queryset = self.filter_by_tag(queryset, t)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def filter_by_title_and_content(self, queryset, q):
        queryset = queryset.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        ).distinct()
        self.paginate_by = None
        return queryset

    def filter_by_tag(self, queryset, t):
        return queryset.filter(tags__value=t)


class CreatePostView(RoleVerificationMixin, CreateView):
    model = Post
    fields = ('title', 'content', 'is_draft', 'tags')
    template_name = 'post_edit.html'
    role_types = (RoleTypes.ADMINISTRATOR, RoleTypes.MANAGER)

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-create')
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdatePostView(RoleVerificationMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ('title', 'content', 'is_draft', 'tags')
    role_types = (RoleTypes.ADMINISTRATOR, RoleTypes.MANAGER)

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-edit', kwargs={'pk': self.get_object().id})
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    role_types = (RoleTypes.ADMINISTRATOR,)

    def get_success_url(self):
        return reverse('blog:index')


class DetailPostView(RoleVerificationMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.id})


class SinglePageView(TemplateView):
    template_name = 'single_page_blog.html'