# forms.py
from django import forms
from facturasieli.models import Verification

class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['comments']

    STATUS_CHOICES = [
        ('vérifiée', 'Vérifiée'),
        ('réjetée', 'Réjetée')
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)