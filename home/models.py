from django.db import models

# Create your models here.
class Restaurant(models.Model):
    """
    A simple model to represent a restaurant
    This will be used to group menu items.
    """
    name = CharField(max_length=200,default="M Restaurant")
    tagline = models.CharField(max_length=300,blank=True)
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='restaurant/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Restaurant Information"
        verbose_name_plural = "Restaurant Information"


    def __str__(self):
        return self.name

@classmethod
def get_restaurant_info(cls):
    """
    Get the active restaurant info for crate default"""
    restaurant = cls.objects.filter(is_active=True).first()
    if not restaurant:
        restaurant= cls.objects.create(
            name="My Restaurant",
            tagline="Welcome to our restaurant"
        )
    return restaurant


class MenuItem(models.Model):
    """
    The model for single menu item (dish)
    Its includes the name, description , price and link to its restaurant
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items') 
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    