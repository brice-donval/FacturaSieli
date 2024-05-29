# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/service_form_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.forms.ServiceForm import ServiceForm
from facturasieli.models import NotificationType, Service
from facturasieli.services.notification_service import send_notification


def handle_service(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    if request.user.is_authenticated:
        print("Authenticated User:", request.user.id)
    else:
        print("User is not authenticated")

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            try:
                service_data = form.cleaned_data
                company_client = request.user.company
                new_service = Service(
                    title=service_data['title'],
                    description=service_data['description'],
                    issue_date=timezone.now(),
                    intervention_start_date=service_data['intervention_start_date'],
                    intervention_end_date=service_data['intervention_end_date'],
                    company_provider=service_data['company_provider'],
                    company_client=company_client
                )
                new_service.save()
                
                #sending notification in-app to the provider
                send_notification(notification_type= NotificationType.DEMANDE_FACTURE,
                                service_title= f"Demande de facture pour l'intervention : {new_service.title}.",
                                company_sender_id= company_client.id,
                                company_receiver_id=new_service.company_provider
                                )
                
                messages.success(request, _("Service created successfully."))
                return redirect('service_page')  # a changer apres création de la page service
            except Exception as e:
                messages.error(request, _("An error occurred while saving the service: %s" % str(e)))
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = ServiceForm()

    return render(request, 'facturasieli/service/service_form.html', {"form": form})
