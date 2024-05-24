# facturasieli/management/commands/init_data.py
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from facturasieli.models import Profile

SUPER_USER_USERNAME = "admin"
USERNAMES = ["alice", "bob"]
PASSWORD = "1234"


class Command(BaseCommand):
    help = "Initializes data for the development of FacturaSieli"

    def handle(self, *args, **options):
        self.clean_database()
        self.create_users()
        self.create_invoices()

    def clean_database(self):
        for model in [User]:
            model.objects.all().delete()

    def create_users(self):
        admin = User.objects.create_superuser(username=SUPER_USER_USERNAME, email="", password=PASSWORD)
        Profile.objects.create(user=admin)
        for username in USERNAMES:
            new_user = User.objects.create_user(username, "", PASSWORD)
            Profile.objects.create(user = new_user)

    def create_invoices(self):
        pass
