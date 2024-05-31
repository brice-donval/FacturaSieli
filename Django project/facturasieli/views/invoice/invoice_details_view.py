# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/invoice/invoice_details_view.py
# Author : Nabil
# ---------------------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service, Invoice


def invoice_details(request, invoice_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    try:
        invoice = get_object_or_404(Invoice, id=invoice_id)
    except:
        return HttpResponseRedirect(reverse('facturasieli:list_invoices'))

    return render(request, 'facturasieli/invoice/invoice_details.html', {'invoice': invoice})

