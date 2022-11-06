from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from django.views.generic import ListView

class ShopHomeView(ListView):
    model = Product
    template_name = 'shop/shop-home.html'
    context_object_name = 'products'
    ordering = ['title']
    paginate_by = 2

class ShopFluView(ListView):
    model = Product
    template_name = 'shop/shop-flu.html'
    context_object_name = 'products'
    ordering = ['title']
    paginate_by = 2
    
    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        return query.filter(category='flu')

class ShopEyeGlassesView(ListView):
    model = Product
    template_name = 'shop/shop-eye-glasses.html'
    context_object_name = 'products'
    ordering = ['title']
    paginate_by = 2
    
    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        return query.filter(category='eye_glasses')

class ShopEyeMedsView(ListView):
    model = Product
    template_name = 'shop/shop-eye-meds.html'
    context_object_name = 'products'
    ordering = ['title']
    paginate_by = 2

    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        return query.filter(category='eye_medicine')

class ShopHeartView(ListView):
    model = Product
    template_name = 'shop/shop-heart.html'
    context_object_name = 'products'
    ordering = ['title']
    paginate_by = 2

    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        return query.filter(category='heart')

class ShopBrandView(ListView):
    model = Product
    template_name = 'shop/shop-brand.html'
    context_object_name = 'products'
    ordering = ['title']
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(brand=self.kwargs['brand_id'])