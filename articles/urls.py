from django.urls import path
from .views import (
    ArticlesHomeView, 
    ArticlesDetailView,
    ArticlesCreateView,
    ArticlesUpdateView,
    ArticlesDeleteView
)

urlpatterns = [
    path('', ArticlesHomeView.as_view(), name='articles-home'),
    path('<int:pk>/', ArticlesDetailView.as_view(), name='articles-detail'),
    path('new/', ArticlesCreateView.as_view(), name='articles-create'),
    path('<int:pk>/update/', ArticlesUpdateView.as_view(), name='articles-update'),
    path('<int:pk>/delete/', ArticlesDeleteView.as_view(), name='articles-delete'),
    ]