# facturasieli/views/service/service_form_view.py
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from facturasieli.forms.ServiceForm import ServiceForm


# author : Morice
def handle_service(request):
    if request.method == 'POST':
        form =ServiceForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            intervention_start_date = form.cleaned_data['intervention_start_date']
            intervention_end_date = form.cleaned_data['intervention_end_date']
            company_client = form.cleaned_data['company_client']
    else:
        form = ServiceForm()
    return render(request, 'facturasieli/service_form.html', {"form":form})
