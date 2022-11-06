from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from products.models import Product

rights = {
    ('user', 'User'),
    ('employee', 'Employee'),
    ('admin', 'Admin')
}

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_id = models.AutoField(primary_key=True)
    user_rights = models.CharField(max_length=20, choices=rights, default='user')
    first_name = models.CharField(max_length=30, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=30, default=None, blank=True, null=True)
    email = models.EmailField(default="example@example.com")
    street_address = models.CharField(max_length=100, default=None, blank=True, null=True)
    city = models.CharField(max_length=100, default=None, blank=True, null=True)
    country = models.CharField(max_length=100, default=None, blank=True, null=True)
    zip_code = models.PositiveBigIntegerField(default=None, validators=[MaxValueValidator(999999999999)], blank=True, null=True)

    def __str__(self):
        return f'{self.first_name, self.last_name}'

class AbstractOrder(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_total(self)    :
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total
    
    @property
    def get_cart_items(self)    :
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    class Meta:
        abstract = True

class Order(AbstractOrder):
    pass

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    @property
    def get_total(self):
        if self.product.price > self.product.discounted_price:
            total = self.product.discounted_price*self.quantity
        else:
            total = self.product.price*self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=30, default=None, null=True)
    last_name = models.CharField(max_length=30, default=None, null=True)
    email = models.EmailField(default="example@example.com")
    street_address = models.CharField(max_length=100, default=None, null=True)
    city = models.CharField(max_length=100, default=None, null=True)
    country = models.CharField(max_length=100, default=None, null=True)
    zip_code = models.PositiveBigIntegerField(default=None, validators=[MaxValueValidator(999999999999)], null=True)

class PreviousOrders(AbstractOrder):
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.transaction_id)

    @classmethod
    def create(cls, customer):
        previous_order = cls(customer=customer)
        return previous_order