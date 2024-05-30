# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Invoice.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Address, Service


class Invoice(models.Model):
    PENDING = 'Pending'
    VERIFIED = 'Verified'
    PAID = 'Paid'
    STATUS_CHOICES = [
        (PENDING, _('Pending')),
        (VERIFIED, _('Verified')),
        (PAID, _('Paid'))
    ]

    invoice_number = models.IntegerField(_("Invoice Number"))
    issue_date = models.DateField(_("Issue Date"))
    due_date = models.DateField(_("Due Date"))
    kind_of_payment = models.CharField(_("Kind of Payment"), max_length=255, default=_('Bank Transfer'))
    name_provider = models.CharField(_("Provider Name"), max_length=255)
    name_client = models.CharField(_("Client Name"), max_length=255)
    amount_excluding_tax = models.FloatField(_("Amount Excluding Tax"))
    tax = models.FloatField(_("Tax"))
    status = models.CharField(_("Status"), max_length=50, choices=STATUS_CHOICES)
    provider_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='invoices_as_provider')
    client_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='invoices_as_client')
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='related_service_invoice', null=True, blank=True)

    def __str__(self):
        return f'Invoice {self.invoice_number} - {self.status}'
