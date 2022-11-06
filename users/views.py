from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned

import json
import datetime
import decimal

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import (
    Order,
    OrderItem,
    ShippingAddress,
    PreviousOrders
)
from products.models import Product

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, 
            instance=request.user.profile
            )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Account updated')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/profile.html', context)

@login_required
def cart(request):
    customer = request.user.profile
    try:
        order, created = Order.objects.get_or_create(customer=customer)
    except MultipleObjectsReturned:
        order = Order.objects.filter(customer=customer).first()
    
    items = order.orderitem_set.all()
    cart_items = order.get_cart_items
    
    context = {
        'current_user': customer,
        'items': items,
        'order': order,
        'cart_items': cart_items,
    }

    return render(request, 'users/cart.html', context)

@login_required
def checkout(request):
    customer = request.user.profile

    try:
        order, created = Order.objects.get_or_create(customer=customer)
    except MultipleObjectsReturned:
        order = Order.objects.filter(customer=customer).first()
    
    items = order.orderitem_set.all()
    
    context = {
        'customer': customer,
        'items': items,
        'order': order,
    }
    
    return render(request, 'users/checkout.html', context)

@login_required
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    qty = int(data['quantity'])

    customer = request.user.profile
    product = Product.objects.get(id=productId)

    try:
        order, created = Order.objects.get_or_create(customer=customer)
    except MultipleObjectsReturned:
        order = Order.objects.filter(customer=customer).first()

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + qty)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)
    elif action == 'remove_all_item_pieces':
        orderItem.quantity = (orderItem.quantity-orderItem.quantity)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.profile

        try:
            order, created = Order.objects.get_or_create(customer=customer)
        except MultipleObjectsReturned:
            order = Order.objects.filter(customer=customer).first()

        for field in data['shipping']:
            if data['shipping'][field] == 'None':
                return JsonResponse('Payment aborted', safe=False)

        total = decimal.Decimal(data['shipping']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            first_name=data['shipping']['first_name'],
            last_name=data['shipping']['last_name'],
            email=data['shipping']['email'],
            street_address=data['shipping']['street_address'],
            city=data['shipping']['city'],
            zip_code=data['shipping']['zip_code'],
            country=data['shipping']['country'],
        )

    if order.complete == True:
        for product_id in data['product_id_qty']:
            product_object = Product.objects.get(id=product_id)
            product_object.number_in_stock -= int(data['product_id_qty'][product_id])
            product_object.save()

        previous_order = PreviousOrders(
            customer=customer,
            order_date=order.order_date,
            transaction_id=order.transaction_id,
            complete=True)
        previous_order.save()

    order.delete()

    return JsonResponse('Payment complete', safe=False)