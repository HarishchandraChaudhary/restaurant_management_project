from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='menu_items/',blank=True,null=True,)

    def __str__(self):
        return self.name
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class OpeningHours(models.Model):
    WEEKDAY=(
        (1,'Monday'),
        (2,'Tuesday'),
        (3,'Wednesday'),
        (4,'Thursday'),
        (5,'Friday'),
        (6,'Saturday'),
        (7,'Sunday')
    )
    restaurant = models.ForeignKey(
        Restaurant,on_delete=models.CASCADE,related_name='opening_hours'
    )
    weekday = models.IntegerField(choices=WEEKDAY)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday','from_hour')
        verbose_name_plural = 'Opening Hours'
        unique_together = ('restaurant','weekday','from_hour')

        def __str__(self):
            return f"{self.get_weekday_display()}:{self.from_hour.strftime('%I:%M %p)}"