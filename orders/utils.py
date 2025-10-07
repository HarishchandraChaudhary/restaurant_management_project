from django.core.mail import send_mail , VadHeaderError
from typing import List

def send_simple_email(
subject:str,
message:str,
recipient_list:List[str]
from_email:str=None) -> bool:

if not recipient_list:
    print('Error: Recipient list is empty.')
    return False

try:
    send_mail(
        subject:subject,
        message=message,
        from_email = from_email,
        recipient_list = recipient_list,
        fail_silently = False,
    )
    print(f"Successfully sent email to:{',.join(recipient_list)}")
    return True
except BadHeaderError:
    print('Error:Email subject or body contained invalid headers.')
    return False
except Exception as e:
    print(f"An unexcepted error occurred while sending email:{e}")
    retur False
