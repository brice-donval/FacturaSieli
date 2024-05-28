# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/show_service_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service


def show_service(request, service_id):
    service = get_object_or_404(Service, id = service_id)
    context = {'service':service}
    return render(request, 'facturasieli/show_service.html', context)
