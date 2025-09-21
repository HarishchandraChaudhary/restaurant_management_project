from django.shortcuts import render

# Create your views here.
from .models import Restaurant, MenuItem

def homepage(request):
    try:
        resutaurant = Restaurant.objects.prefetch_related('opening_hours').get(pk=1)
    except Restaurant.DoesNotExist:
        resutaurant = None
    query = request.GET.get('q','')
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    return render(request,'homepage.html',context)
