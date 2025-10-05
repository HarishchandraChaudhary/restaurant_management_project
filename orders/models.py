from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


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
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name ='orders', verbose_name='Customers')
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10,decimal_places2)



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

class Coupon(models.Model):
    code = models.CharField(max_length=20,unique=True)
    discount_percent = models.IntegerField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural='Coupons'


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank==True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='Category')




class Coupon(models.Model):
    code = models.CharField(max_length=50,
    unique=True,
    verbose_name='Coupon Code')

    discount_percentage = models.DecimalField(

        max_digits=3,
        decimal_places=2,
        validators = [MinValueValidator(Decimal('0.01')),MaxValueValidator(Decimal('0.02'))]
        verbose_name = 'Discount Percentage (0.01 to 0.99)'
        help_text = 'Stored as a decimal (0.10 for 10% off)'

    )
    valid_from = models.DateField(
        verbose_name = 'Valid Form'
    )

    is_active = models.BooleanField(
        default = True,
        verbose_name  = "Is Active"


    )
    valid_until = models.DateField(
        verbose_name = 'Valid Until'
    )

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural='Coupons'
        ordering = ['valid_until']

    def __str__(self):
        return f "{self.code}({self.discount_percentage * 100}%)"
