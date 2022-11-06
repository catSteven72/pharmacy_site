from django.urls import path
from .views import (
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('new/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)