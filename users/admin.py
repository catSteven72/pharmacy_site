from django.contrib import admin
from .models import (
    UserProfile,
    Order,
    OrderItem,
    PreviousOrders
)

admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PreviousOrders)