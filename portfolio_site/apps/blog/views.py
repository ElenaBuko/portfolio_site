from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse

from apps.blog.models import Post


class ListPostView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    # paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
            self.paginate_by = None
        return queryset


class CreatePostView(CreateView):
    model = Post
    fields = ('title', 'content', 'is_draft', 'tags')
    template_name = 'post_edit.html'

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-create')
        return context


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ('title', 'content', 'is_draft', 'tags')

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-edit', kwargs={'pk': self.get_object().id})
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse('blog:index')


class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.id})
