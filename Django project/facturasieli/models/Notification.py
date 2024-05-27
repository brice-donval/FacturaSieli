# facturasieli/models/Notification.py
from django.db import models
from facturasieli.models.Company import Company
from facturasieli.models.NotificationType import NotificationType
from django.utils.translation import gettext_lazy as _

class Notification(models.Model):
    send_at = models.DateField(_("Send At"))
    type = models.IntegerField(_("Type"), choices=NotificationType.choices, default=NotificationType.DEMANDE_FACTURE)
    service_title = models.CharField(_("Service Title"), max_length=255)
    company_sender = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_sender')
    company_receiver = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_receiver')
