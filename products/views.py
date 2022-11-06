# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Product

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import Product
from django.views.generic import (
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = [
        'title', 
        'description', 
        'price', 
        'discount_percent', 
        'picture', 
        'number_in_stock', 
        'category', 
        'brand'
        ]

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        product = self.get_object()
        if (self.request.user.profile.user_rights == 'admin') or (self.request.user.profile.user_rights == 'employee'):
            return True
        return False

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = [
        'title', 
        'description', 
        'price', 
        'discount_percent', 
        'picture', 
        'number_in_stock', 
        'category', 
        'brand'
        ]

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        product = self.get_object()
        if (self.request.user.profile.user_rights == 'admin') or (self.request.user.profile.user_rights == 'employee'):
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('shop-home')

    def test_func(self):
        product = self.get_object()
        if (self.request.user.profile.user_rights == 'admin') or (self.request.user.profile.user_rights == 'employee'):
            return True
        return False