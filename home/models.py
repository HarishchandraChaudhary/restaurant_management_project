from django.db import models

# Create your models here.
class Restaurant(models.Model):
    """
    A simple model to represent a restaurant
    This will be used to group menu items.
    """
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    The model for single menu item (dish)
    Its includes the name, description , price and link to its restaurant
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items') 
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    