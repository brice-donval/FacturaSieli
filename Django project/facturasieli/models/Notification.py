# facturasieli/models/Notification.py
from django.db import models

from facturasieli.models.Company import Company
from facturasieli.models.NotificationType import NotificationType


class Notification(models.Model):
    send_at = models.DateField()
    type =models.IntegerField(choices=NotificationType, default=NotificationType.DEMANDE_FACTURE)
    service_title = models.CharField(max_length=255)
    company_sender = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_sender')
    company_receiver = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_receiver')
