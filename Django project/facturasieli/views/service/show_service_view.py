from django.shortcuts import render, redirect,get_object_or_404
from django.utils.translation import gettext_lazy as _
from ...models import Service


def show_service(request, service_id):
    service = get_object_or_404(Service, id = service_id)
    context = {'service':service}
    return render(request, 'facturasieli/show_service.html', context)