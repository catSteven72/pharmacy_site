from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import Article
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )

class ArticlesHomeView(ListView):
    model = Article
    template_name = 'articles/articles-home.html'
    context_object_name = 'articles'
    ordering = ['-post_date']
    paginate_by = 1

class ArticlesDetailView(DetailView):
    model = Article

class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = [
        'title', 
        'content',
        'picture'
        ]

    def get_success_url(self):
        return reverse('articles-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        article = self.get_object()
        if (self.request.user.profile.user_rights == 'admin') or (self.request.user.profile.user_rights == 'employee'):
            return True
        return False


class ArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = [
        'title', 
        'content',
        'picture'
        ]

    def get_success_url(self):
        return reverse('articles-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        article = self.get_object()
        if (self.request.user.profile.user_rights == 'admin') or (self.request.user.profile.user_rights == 'employee'):
            return True
        return False

class ArticlesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article

    def get_success_url(self):
        return reverse('articles-home')

    def test_func(self):
        article = self.get_object()
        if (self.request.user.profile.user_rights == 'admin') or (self.request.user.profile.user_rights == 'employee'):
            return True
        return False