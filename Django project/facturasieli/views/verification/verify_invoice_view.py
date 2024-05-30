# facturasieli/views/verify_invoice_view.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Invoice, Verification
from facturasieli.forms import VerificationForm
#from facturasieli.utils import is_company_verifier_or_admin

@login_required
#@user_passes_test(is_company_verifier_or_admin)
def verify_invoice_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.invoice = invoice
            verification.verified_by = request.user.profile
            verification.save()

            invoice.status = form.cleaned_data['status']
            invoice.save()

            return JsonResponse({'message': _('Invoice status updated successfully')}, status=200)
    else:
        form = VerificationForm()

    return render(request, 'facturasieli/verification/verify_invoice.html', {'invoice': invoice, 'form': form})
