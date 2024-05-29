# facturasieli/forms/InvoiceForm.py
from django import forms
from facturasieli.models.Invoice import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoice_number', 'issue_date', 'due_date', 'kind_of_payment',
            'name_provider', 'name_client', 'amount_excluding_tax', 'tax',
            'status', 'provider_address', 'client_address'
        ]