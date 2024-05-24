# facturasieli/models/Service.py
from django.db import models

from facturasieli.models.Company import Company
from facturasieli.models.Invoice import Invoice


class Service(models.Model):
    DEMANDE_DE_FACTURATION_ENVOYEE = 'Demande de facturation envoyée'
    TERMINE = 'Terminé'
    STATUS_CHOICES = [
        (DEMANDE_DE_FACTURATION_ENVOYEE, 'Demande de facturation envoyée'),
        (TERMINE, 'Terminé')
    ]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    issue_date = models.DateField()
    intervention_start_date = models.DateField()
    intervention_end_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    company_provider = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='provided_services')
    company_client = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='received_services')
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name='service', null=True, blank=True)

    def __str__(self):
        return self.title
