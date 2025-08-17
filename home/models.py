from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Restaurant Information"
        verbose_name_plural = "Restaurant Information"
        
