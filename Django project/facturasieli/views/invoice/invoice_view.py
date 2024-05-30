# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/invoice/invoice_view.py
# Author : Margaux
# ---------------------------------------------------------------------------

import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from facturasieli.forms.InvoiceForm import InvoiceForm
from facturasieli.models import Service

logger = logging.getLogger(__name__)

def invoice_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.service = service
            invoice.save()
            messages.success(request, "Invoice saved successfully.")
            url = reverse('facturasieli:service', kwargs={'company_id': service.company_provider.id})
            return redirect(url)
        else:
            logger.error("Form is not valid: %s", form.errors)
            messages.error(request, "There were errors in your form. Please correct them and try again.")
    else:
        form = InvoiceForm()
    
    return render(request, 'facturasieli/invoice_form.html', {'form': form, 'service': service})

#def invoice_success(request):
#    return render(request, 'facturasieli/invoice_success.html')
