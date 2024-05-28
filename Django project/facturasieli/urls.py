# facturasieli/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path

from facturasieli import views


app_name = 'facturasieli'
urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),

    path('custom_login/', views.custom_log_in, name='custom_log_in'),
    path('otp_validation/', views.otp_validation, name='otp_validation'),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='log_in'),

    path('logout/', views.log_out, name='log_out'),
    path('goodbye/', views.goodbye, name='goodbye'),

    path('public_profile/<int:user_id>/', views.public_profile, name='public_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('service_form/', views.handle_service, name='service_form'),
    path('service/<int:company_id>/', views.display_service, name='service'),

    path('invoices/<int:invoice_id>/verify/', views.verify_invoice_view, name='verify_invoice'),
]
