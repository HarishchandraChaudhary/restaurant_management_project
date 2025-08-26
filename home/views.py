from django.shortcuts import render
from .models import RestaurantInfo

def home(request):
    try:
        info = RestaurantInfo.objects.get(pk=1)
        restaurant_name = "Our Restaurant "

        context = {
            'restaurant_name':restaurant_name
        }
        return render(request,'templates/homepage.html')