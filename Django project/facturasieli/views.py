# facturasieli/views.py
import os
import secrets

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.forms import OTPModelForm, ProfileForm
from facturasieli.models import OTPModel, Profile


# --------------------------------------------------------------------------- #
#                                  I N D E X                                  #
# --------------------------------------------------------------------------- #

def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    context = {}
    return render(request, 'facturasieli/index.html', context)


# --------------------------------------------------------------------------- #
#                           R E G I S T R A T I O N                           #
# --------------------------------------------------------------------------- #

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


def create_otp(user: User):
    OTPModel.objects.filter(user=user.id).delete()
    new_otp = OTPModel(user=user, otp=secrets.token_urlsafe(4))
    new_otp.save()
    return new_otp


def send_otp_mail(otp_instance: OTPModel):
    subject: str =  'FacturaSieli - ' + _('Authentication')
    message: str =  _('Your one time password: - ') + otp_instance.otp
    from_email: str =  'noreply@facturasieli.com'
    recipient_list: list[str] =  [otp_instance.user.email]
    return send_mail(subject, message, from_email, recipient_list, fail_silently=True)


def otp_validation(request: HttpRequest):
    if request.method == 'GET':
        form = OTPModelForm()
        return render(request, 'registration/otp_validation.html', {'form': form})

    form = OTPModelForm(request.POST)
    if not form.is_valid():
        return render(request, 'registration/otp_validation.html', {'form': form})

    user_otp = form.cleaned_data['otp']
    pretended_user_id = request.session.get('pretended_user_id', '')
    if not pretended_user_id:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    otp_instance = OTPModel.objects.filter(
        otp=user_otp,
        user=pretended_user_id).first()
    if otp_instance:
        if otp_instance.expiration_timestamp > timezone.now():
            login(request, otp_instance.user)
            return HttpResponseRedirect(reverse('facturasieli:index'))
        else:
            return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    return render(request, 'registration/otp_validation.html', {'form': form})


def custom_log_in(request: HttpRequest):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/custom_login.html', {'form': form})
    
    form = AuthenticationForm(request, request.POST)
    if not form.is_valid():
        return render(request, 'registration/custom_login.html', {'form': form})

    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return render(request, 'registration/custom_login.html', {'form': form})

    profile = get_object_or_404(Profile, user = user.id)
    if not profile.enable_2fa:
        login(request, user)
        return HttpResponseRedirect(reverse('facturasieli:index'))
    else:
        otp_instance = create_otp(user)
        send_otp_mail(otp_instance)
        request.session['pretended_user_id'] = user.id
        return HttpResponseRedirect(reverse('facturasieli:otp_validation'))


def log_out(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('facturasieli:goodbye'))
    return render(request, 'registration/logout.html')


# --------------------------------------------------------------------------- #
#              R E G I S T R A T I O N    T R A N S I T I O N S               #
# --------------------------------------------------------------------------- #

def welcome(request: HttpRequest):
    return render(request, 'registration/transitions/welcome.html')


def goodbye(request: HttpRequest):
    return render(request, 'registration/transitions/goodbye.html')


# --------------------------------------------------------------------------- #
#                                P R O F I L E                                #
# --------------------------------------------------------------------------- #

def public_profile(request: HttpRequest, user_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    user_to_show = get_object_or_404(User, pk=user_id)
    profile_to_show = get_object_or_404(Profile, user=user_to_show.id)

    context = {
        'profile': profile_to_show,
    }
    return render(request, 'facturasieli/public_profile.html', context)


def edit_profile(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    old_avatar = request.profile.avatar.path

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.profile)
        if form.is_valid():
            if request.FILES:
                if not 'default_avatar' in old_avatar:
                    try:
                        os.remove(old_avatar)
                    except:
                        pass
            form.save()

            request.user.email = request.POST.get('email', '')
            request.user.save()

            return HttpResponseRedirect(reverse('facturasieli:index'))
    else:
        form = ProfileForm(
            initial={'email': request.user.email},
            instance=request.profile
        )

    context = { 'form': form }
    return render(request, 'facturasieli/edit_profile.html', context)

