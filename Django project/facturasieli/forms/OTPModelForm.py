# facturasieli/forms/OTPModelForm.py
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from facturasieli.models import OTPModel


class OTPModelForm(ModelForm):
    class Meta:
        model = OTPModel
        fields = ['otp']
