from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name  = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places = 2)
    # The __str__ methos is important for making objects human readable in the admin.
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES= (
        ('pending','Pending'),
        ('processing','Processing'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('canceled','Canceled'),
    )

    customer = models.ForeignKey(User,on_delete=models.CASCADE)

    order_items = models.ManyToManyField(MenuItem,through='OrderItem')

    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order # {self.id} for {self.customer.username}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.menu_item.name} for Order #{self.order.id}"


class OrderStatus(models.Model):
    name= models.CharField(max_length=50,unique = True,verbose_name='Status Name',help_text = 'The unique of the order status.')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'
        ordering = ['name']