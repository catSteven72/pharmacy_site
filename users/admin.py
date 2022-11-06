from django.contrib import admin
from .models import (
    UserProfile,
    Order,
    OrderItem,
)

admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
