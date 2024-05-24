# facturasieli/models/Invoice.py
from django.db import models

from facturasieli.models.Address import Address


class Invoice(models.Model):
    EN_ATTENTE = 'en attente'
    VERIFIEE = 'vérifiée'
    PAYEE = 'payée'
    STATUS_CHOICES = [
        (EN_ATTENTE, 'en attente'),
        (VERIFIEE, 'vérifiée'),
        (PAYEE, 'payée')
    ]

    invoice_number = models.IntegerField()
    issue_date = models.DateField()
    due_date = models.DateField()
    kind_of_payment = models.CharField(max_length=255, default='Virement')
    name_provider = models.CharField(max_length=255)
    name_client = models.CharField(max_length=255)
    amount_excluding_tax = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    provider_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='invoices_as_provider')
    client_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='invoices_as_client')

    def __str__(self):
        return f'Invoice {self.invoice_number} - {self.status}'
