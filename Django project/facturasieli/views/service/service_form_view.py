from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# author : Morice


def handle_service(request):
    if request.method == 'POST':
        pass
    return render(request, 'facturasieli/service_form.html')
