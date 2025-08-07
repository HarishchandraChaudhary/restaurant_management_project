from django.contrib import admin

from .models import MenuItem,Order,OrderItem

class OrderItemInline(admin.TabularInline):
    # This links the inline form to our OrderItem model.
    model = OrderItem
    # 'extra' specifies which fields to display
    extra = 1
    # We can also specify which fields to display.
    fields = ('menu_item','quantity') 

class OrderAdmin(admin.ModelAdmin):
    # 'list_display' controls which fields are shown in the main list view.
    list_display  = ('id','customer','total_amount','status','created_at')

    #'list_filter' adds a sidebar filter for the specified fields.
    seach_fields = ('customer__username','status')

    # inline tells Django to display the OrderItemInline class on this page.
    inlines = [OrderItemInline]

# To register a model with a custom admin class,you pas both the model and the page.
admin.site.register(Order,OrderAdmin)

# To register a model with the default admin, you simply pass the model
admin.site.register(MenuItem)

