from django.shortcuts import render

# Create your views here.
import requests

def home_view(request):
    menu_items=[]
    try:
        api_url = "http://your-api-menu-endpoint/menu/"
        response = request.get(api_url)
        response.raise_raise_for_status()
        menu_items = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error Fetching menu:{e}")
    
    context = {
        'menu_items' :menu_items
    }
    return render(request, 'menu.html',context)