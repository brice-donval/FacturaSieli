# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/invoice/list_invoices_view.py
# Author : Nabil
# ---------------------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service, Invoice


def list_invoices(request, company_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    outgoing_invoices = Invoice.objects.filter(service__company_provider_id=company_id)
    incoming_invoices = Invoice.objects.filter(service__company_client_id=company_id)

    context = {'outgoing_invoices':outgoing_invoices, 'incoming_invoices':incoming_invoices}
    return render(request, 'facturasieli/invoice/list_invoices.html', context)

