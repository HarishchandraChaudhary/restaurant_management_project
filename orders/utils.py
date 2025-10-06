import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLoger(__name__)
def send_order_confirmation_email(order_id:int,customer_email:str,order:int):
    plain_message = (
        f"Thank you for your order! Your order details are confirmed.\n\n"
        f"Order ID:{order_id}\n",
        f"Summary:\n{order_summary}\n"
        f"Total Price:${total_price:.2f}\n\n"
        f"Please contact us if you have any questions.\n"

    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]

    try:
        send_mail(
            subject = subject,
            message = plain_message,
            from_email = from_email,
            recipient_list=recipient_list,
            fail_silently = False

        )
        logger.info(f"Order confirmation email sent successfully for Orders)"
        return True

        except Exception as e:
            logger.error(f"Failed to send order confirmation email for Order In.)"
            return False