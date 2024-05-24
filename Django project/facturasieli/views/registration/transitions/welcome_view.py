# facturasieli/views/registration/transitions/welcome_view.py
from django.http import HttpRequest
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def welcome(request: HttpRequest):
    return render(request, 'registration/transitions/welcome.html')
