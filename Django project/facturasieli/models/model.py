from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Role(models.Model):
    role = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.role

class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=255)
    addings = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.number} {self.street}, {self.city}, {self.country}"


class Company(models.Model):
    siret = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='companies')

    def __str__(self):
        return self.name

class User(AbstractBaseUser):
    objects = BaseUserManager()
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
    password = models.CharField(max_length=255)
    role = models.ManyToManyField(Role, related_name="users")

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
        return f"Invoice {self.invoice_number} - {self.status}"

class Service(models.Model):
    DEMANDE_DE_FACTURATION_ENVOYE = 'Demande de facturation envoyé'
    TERMINE = 'Terminé'
    STATUS_CHOICES = [
        (DEMANDE_DE_FACTURATION_ENVOYE, 'Demande de facturation envoyé'),
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

class NotificationType(models.IntegerChoices):
    DEMANDE_FACTURE = 1, 'Demande de facture'
    FACTURE_SOUMISE = 2, 'Facture soumise'
    FACTURE_VERIFIEE = 3, 'Facture verifée'
    FACTURE_REJETE =  4, 'Facture réjétée'
    FACTURE_PAYE = 5, 'Facture payé'

class Notification(models.Model):
    send_at = models.DateField()
    type =models.IntegerField(choices=NotificationType, default=NotificationType.DEMANDE_FACTURE)
    service_title = models.CharField(max_length=255)
    company_sender = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_sender')
    company_receiver = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_receiver')