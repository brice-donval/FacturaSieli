# facturasieli/models/Verification.py
from django.db import models
from facturasieli.models.User import User
from facturasieli.models.Invoice import Invoice
from django.utils.translation import gettext_lazy as _

class Verification(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='verifications')
    verified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verifications_user')
    date_verified = models.DateTimeField(_("Date Verified"), auto_now_add=True)
    comments = models.TextField(_("Comments"))

    def __str__(self):
        return f"{self.invoice.invoice_number} by {self.verified_by.email}"
