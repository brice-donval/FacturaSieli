# facturasieli/forms/ProfileForm.py
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Profile


class ProfileForm(ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'enable_2fa']

    def clean(self):
        enable_2fa = self.cleaned_data['enable_2fa']
        email = self.cleaned_data['email']
        if enable_2fa and not email:
            raise ValidationError(_('Your e-mail address is necessary to enable the two-factor authentication!'))
