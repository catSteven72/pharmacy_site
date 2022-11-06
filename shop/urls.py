from django.urls import path
from .views import (
    ShopHomeView,
    ShopFluView,
    ShopHeartView,
    ShopEyeGlassesView,
    ShopEyeMedsView,
    ShopBrandView,
)

urlpatterns = [
    path('', ShopHomeView.as_view(), name='shop-home'),
    path('shop-flu', ShopFluView.as_view(), name='shop-flu'),
    path('shop-eye-glasses', ShopEyeGlassesView.as_view(), name='shop-eye-glasses'),
    path('shop-eye-medicine', ShopEyeMedsView.as_view(), name='shop-eye-medicine'),
    path('shop-heart', ShopHeartView.as_view(), name='shop-heart'),
    path('shop-brand/<str:brand_id>', ShopBrandView.as_view(), name='shop-brand'),
    ]