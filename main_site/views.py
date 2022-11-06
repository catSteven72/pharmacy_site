from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def home(request):
    return render(request, 'main_site/home.html')

def about(request):
    return render(request, 'main_site/about.html')

def privacy(request):
    return render(request, 'main_site/privacy.html')

def careers(request):
    return render(request, 'main_site/careers.html')

def search_results(request):
    if request.method == "POST":
        search_request = request.POST['search_request']
        products = Product.objects.filter(title__contains=search_request)

        if len(products) == 0:
            context = {
            'searched': search_request,
            'products': products,
        }
        
        context = {
            'searched': search_request,
            'products': products,
        }

        return render(request, 'main_site/search-results.html', context)
    
    else:
        return render(request, 'main_site/search-results.html', {})