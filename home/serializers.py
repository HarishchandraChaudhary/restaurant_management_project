from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    clas Meta:
    model = MenuCategory
    fields = ['id','name']
