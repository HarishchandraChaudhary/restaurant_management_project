import secrets
import string
form .models impot Coupon

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits
    while True:
        if not Coupon.objects.filter(code=code).exists():
            return code
