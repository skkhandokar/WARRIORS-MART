from django.shortcuts import render
from items.models import Product
# Create your views here.


def home(request):
    products = Product.objects.all().filter(is_available=True)
    return render(request, 'index.html', context={'products': products})