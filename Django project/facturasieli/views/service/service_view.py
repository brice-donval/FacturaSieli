# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/service_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.shortcuts import render,get_list_or_404
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.http import  HttpResponseRedirect
from facturasieli.models import Service
from django.urls import reverse


def display_service(request,company_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    services = get_list_or_404(Service, company_client=company_id)
    print(services)
    return render(request, 'facturasieli/service/service.html', {'services': services})
