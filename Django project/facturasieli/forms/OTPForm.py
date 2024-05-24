# facturasieli/forms/OTPForm.py
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from facturasieli.models import OTP


class OTPForm(ModelForm):
    class Meta:
        model = OTP
        fields = ['otp']
