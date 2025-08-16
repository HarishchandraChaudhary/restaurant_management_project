from django.shortcuts import render
from django.conf import settings
from .models import Restaurant

def index(request):
    """
    HomePage view with restaurant  information
    """
    try:
        restaurant = Restaurant.get_restaurant_info()
        context = {
            'restaurant_name': restaurant.name,
            'restaurant_tagline':restaurant.tagline,
            'restaurant_phone':restaurant.phone,
            'restaurant_email':restaurant.email,
            'restaurant_address':restaurant.address,
            'restaurant_logo':restaurant.logo,
            'data_source':'database'
        }
    except Exception as e:
        context = {
            'restaurant_name':getattr(settings,'RESTAURANT_NAME','My Restaurant'),
            'restaurant_tagline':getattr(settings,'RESTAURANT_TAGLINE','Welcome to our restaurant'),
            'restaurant_phone':getattr(settings,'RESTAURANT_PHONE',''),
            'restaurant_email':getattr(settings,'RESTAURANT_EMAIL',''),
            'restaurant_address':getattr(settings,'RESTAURANT_ADDRESS',''),
            'restaurant_logo':None,
            'data_source':'settings'
        }

    return render(request,'home/index.html',context)

def about(request):
    """
    About page view
    """
    try:
        restaurant = Restaurant.get_restaurant_info()
        context = {
            'restaurant':restaurant,
        }
    except  Exception as e:
        context = {
            'restaurant_name':getattr(settings,'RESTAURANT_NAME','My Restaurant'),
        return render(request,'home/about.html',context)
        }
def home_page_view(request):
    return render(request,'home/index.html')


def about(request):
    return render(request,'home/about.html')

def _404(request):
    return render(request,'template/404.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    context = {
        'restaurant_name':'Coding-Themed Art Prints Restaurant',
        'Welcome_message':'Experience the finest dining with our unique coding-themed atomsphere!'
        

    }
    return render(request,'home/index.html',context)