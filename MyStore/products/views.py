from django.shortcuts import render

# Create your views here.
def products (request):
    return render (request , 'products/products.html')

def product_detail():
    pass