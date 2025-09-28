from django.db import models
from django import forms
class Restaurant(models.Model):
    name = models.CharFie
    ld(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        
        return self.name

    class Meta:
        verbose_name = "Restaurant Information"
        verbose_name_plural = "Restaurant Information"
        
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name



class RestaurantLocation(models.Model):
    """
    A Django model to store a restaurant's location details.
    """
    address = model.CharField(max_length=255,help_text = "The street address of the restaruant ")
    city = models.CharField(max_length=100,help_text="The city where the restaurant located")
    state = models.CharField(max_length=100,help_text="The state where the restaurant is located.")
    zip_code = models.CharField(max_length=20, help_text="The zip code of the restaurant is available")
    
    def __str__(self):
        """
        Returns a string representation of the model instance.
        """
        return f"{self.address}, {self.city},{self.state}{self.zip_code}"
    
    class Meta:
        """
        Meta options for the model
        """
        verbose_name="Restaurant Location"
        verbose_name_plural = "Restaurant Locations"



class ContactSubmission(model.Model):
    """
    A simple Django model to store constact form submissions.
    """
    name = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)



class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name='Cateogry Name',help_text='The unique name of the meny category')
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Menu Category'
        verbose_name_plural = 'Menu Categories'
        ordering = ['name']
