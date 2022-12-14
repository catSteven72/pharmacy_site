from django.urls import path
from .views import (
    ArticlesHomeView, 
    ArticlesDetailView,
    ArticlesCreateView,
    ArticlesUpdateView,
    ArticlesDeleteView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ArticlesHomeView.as_view(), name='articles-home'),
    path('<int:pk>/', ArticlesDetailView.as_view(), name='articles-detail'),
    path('new/', ArticlesCreateView.as_view(), name='articles-create'),
    path('<int:pk>/update/', ArticlesUpdateView.as_view(), name='articles-update'),
    path('<int:pk>/delete/', ArticlesDeleteView.as_view(), name='articles-delete'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)