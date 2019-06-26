from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import render
from .models import *
# Create your views here.

def dashboard(request):
    # category.objects.all()
    # info = category.objects.all()
    # print(info)
    return render(request, 'dashboard/dashboard.html')

def contact_us(request):
    return  render(request, 'contact_us/contact_us.html')

def cart(request):
    return render(request, 'cart/cart.html')



