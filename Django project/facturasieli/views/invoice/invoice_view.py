# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/invoice/invoice_view.py
# Author : Margaux
# ---------------------------------------------------------------------------

from django.shortcuts import render, redirect

from facturasieli.forms.InvoiceForm import InvoiceForm


def invoice_view(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturasieli:invoice_success')  # Redirige vers une page de succès après soumission
    else:
        form = InvoiceForm()
    
    return render(request, 'facturasieli/invoice_form.html', {'form': form})

def invoice_success(request):
    return render(request, 'facturasieli/invoice_success.html')
