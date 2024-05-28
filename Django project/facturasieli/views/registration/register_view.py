# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/register_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Profile


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            return HttpResponseRedirect(reverse('facturasieli:welcome'))
    else:  
        form = UserCreationForm()   

    context = { 'form': form }
    return render(request, 'registration/register.html', context)
