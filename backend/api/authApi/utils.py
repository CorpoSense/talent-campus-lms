from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from api import settings
def sendActivationEmail(user):
    tokenToSend = Token.objects.get_or_create(user)
    activation_link = f"http://your-domain.com/activate/{tokenToSend.key}"

    # Email subject and message
    subject = 'Activate your account'
    message = f'Hi {user.username},\n\nPlease click the link below to activate your account:\n{activation_link}'

    # Send the email
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # From email
        [user.email],  # To email
        fail_silently=False,
    )