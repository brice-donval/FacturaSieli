# facturasieli/forms/VerificationForm.py
from django import forms

from facturasieli.models import Verification


class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['comments']

    STATUS_CHOICES = [
        (1, 'Verified'),
        (2, 'rejected')
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)
