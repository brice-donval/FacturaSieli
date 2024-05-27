# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from facturasieli.models import Invoice, Verification
from facturasieli.forms import VerificationForm

@login_required
def verify_invoice_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.invoice = invoice
            verification.verified_by = request.user
            verification.save()
            
            invoice.status = form.cleaned_data['status']
            invoice.save()

            return JsonResponse({'message': _('Invoice status updated successfully')}, status=200)
    else:
        form = VerificationForm()
    
    return render(request, 'verify_invoice.html', {'invoice': invoice, 'form': form})
