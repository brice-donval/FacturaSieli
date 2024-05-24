# facturasieli/models/utils.py
from datetime import timedelta

from django.utils import timezone

from facturasieli.conf import OTP_VALIDITY_DURATION


def get_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/avatar
    return 'user_{0}/avatar'.format(instance.user.id)


def compute_expiration_timestamp():
    return timezone.now() + timedelta(seconds=OTP_VALIDITY_DURATION)
