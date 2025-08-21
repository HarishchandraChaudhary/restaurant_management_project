from django.conf import settings
from datetime import datetime

def restaurant_info(request):
    """
    Add restaurant information to all template contexts
    """
    return {
        'restaurant_name':getattr(settings,'RESTAURANT_NAME','Restaurant'),
        'restaurant_phone':getattr(settings,'RESTAURANT_PHONE','N/A'),
        
    }

def site_info(request):
    return {
        'current_year':datetime.now().year,
        'site_name':'Restaurant Management System',
        'company_name':'Your Restaurant Company',
        'contact_email':'info@restaurant.com',
        'contact_phone':'+91 98574 12345',
    }
    