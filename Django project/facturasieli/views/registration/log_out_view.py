# facturasieli/views/registration/log_out_view.py
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def log_out(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('facturasieli:goodbye'))
    return render(request, 'registration/logout.html')
