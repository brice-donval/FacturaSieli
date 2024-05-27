from django import forms
from ..models.Service import Service
from django.utils.translation import gettext_lazy as _

# Author Morice
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title", "description", "intervention_start_date", "intervention_end_date", "company_client"]  # Corrected typo here
        labels = {
            'title': _('Service Title:'),
            'description': _('Description:'),
            'intervention_start_date': _('Start of the service:'),
            'intervention_end_date': _('End of the service:'),
            'company_client': _('Company:'),
        }
