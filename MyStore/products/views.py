from django.shortcuts import render

# Create your views here.

all_products = [
    { 'title' : 'product1',
      'image' : 'pic1.jpg',
     'summary': 'summary1',
     'slug'   : 'product1'
    },
    { 'title' : 'product2',
      'image' : 'pic2.jpg',
     'summary': 'summary2',
     'slug'   : 'product2'
    },
    { 'title' : 'product3',
      'image' : 'pic3.jpg',
     'summary': 'summary3',
     'slug'   : 'product3'
    }
    ]



def products (request):
    return render (request , 'products/products.html' , {'products' : all_products })

def product_detail(request , slug):
    return render (request , 'products/product_detail.html' )