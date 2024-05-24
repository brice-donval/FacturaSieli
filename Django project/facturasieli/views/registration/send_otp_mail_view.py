# facturasieli/views/registration/send_otp_mail_view.py
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from facturasieli.models import OTPModel


def send_otp_mail(otp_instance: OTPModel):
    subject: str =  'FacturaSieli - ' + _('Authentication')
    message: str =  _('Your one time password: - ') + otp_instance.otp
    from_email: str =  'noreply@facturasieli.com'
    recipient_list: list[str] =  [otp_instance.user.email]
    return send_mail(subject, message, from_email, recipient_list, fail_silently=True)
