from django.db import models

# Create your models here.
class Order(models.Model):
  order_id = models.AutoField(primary_key=True)
  customer_name = models.CharField(max_length=100)
  note = models.TextField(blank=True,null=True)
  total_order_amount = models.FloatField(default=0.0)
  is_paid = models = BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return f"Order #{self.order_id} by {self.customer_name}"
class OrderItem(models.Model):
  order = models.CharField(Order,on_delete=models.CASCADE, related_name="items")
  item_name = models.CharField(max_length=100)
  qnty = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.qynty} * {self.item_name} for Order #{self.order.order_name}"
