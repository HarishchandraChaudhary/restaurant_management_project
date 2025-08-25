from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name','tagline','is_active','created_at']
    list_filter = ['is_active','created_at']
    search_fields = ['name','tagline']
    fields = ['name','tagline','phone','email','address','logo','is_active']
    
admin.site.register(Feedback)
