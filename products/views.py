from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HardCodeMenuView(APIView):
    """
    An API view to reterivew a hard code list menu items.
    This views not interact with databses.
    """
    def get(self,request.format=None):
        """
        Returns a hardcoded list menu items.
        """
        menu_data = [
            {
            'name':'Paneer Tikka Masala',
            'description':'Cubes of paneer (Indian Chese)coocked in rich creamy tomato gravy.',
            'price':'9.75'
            },
            {
            'name':'Chicken Biryani',
            'description':'Aromatic basmati rice  coocked with tender chicken pieces and exotic spices.',
            'price':'3.00'
            },
            {
                'name':'Gulab Jamun',
                'description':'Deep fried milk solids soaked in a sweet rose flaoured syrup. ',
                'price':'5.00'
            }
        ]
        return Response(menu_data,status=status.HTTP_200_OK)

def homepage_view(request):
    try:
        restaurant = Restaurant.objects.first()
        address = restaurant.address 
    except Restaurant.DoesNotExist:
        address = "Address not available."
        context = {
            'restaurant_address':address
        }
        return render(request,'homepage_view.html',context)
