# facturasieli/views/registration/transitions/goodbye_view.py
from django.http import HttpRequest
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def goodbye(request: HttpRequest):
    return render(request, 'registration/transitions/goodbye.html')
