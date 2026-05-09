from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    #return HttpResponse("You're at the products page.")
    return render(request, 'index.html', {'products': products})

def sale(request):
    return HttpResponse("Sales item here...");