# facturasieli/views/registration/create_otp_view.py
import secrets

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from facturasieli.models import OTPModel


def create_otp(user: User):
    OTPModel.objects.filter(user=user.id).delete()
    new_otp = OTPModel(user=user, otp=secrets.token_urlsafe(4))
    new_otp.save()
    return new_otp
