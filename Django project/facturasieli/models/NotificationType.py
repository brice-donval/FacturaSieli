# facturasieli/models/NotificationType.py
from django.db import models


class NotificationType(models.IntegerChoices):
    DEMANDE_FACTURE = 1, 'Demande de facture'
    FACTURE_SOUMISE = 2, 'Facture soumise'
    FACTURE_VERIFIEE = 3, 'Facture vérifée'
    FACTURE_REJETE = 4, 'Facture rejetée'
    FACTURE_PAYE = 5, 'Facture payée'
