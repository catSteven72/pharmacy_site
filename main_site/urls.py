from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search_results, name='search-results'),
    path('about', views.about, name='about'),
    path('privacy', views.privacy, name='privacy'),
    path('careers', views.careers, name='careers'),
    ]