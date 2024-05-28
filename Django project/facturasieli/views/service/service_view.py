from django.shortcuts import render, redirect,get_list_or_404
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from ...models import Service


def display_service(request,company_id):
    services = get_list_or_404(Service, company_client=company_id)
    print(services)
    return render(request, 'facturasieli/service.html', {'services': services})
