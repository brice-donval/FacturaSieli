# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Profile.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from facturasieli.models.utils import get_avatar_path


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(_("Avatar"), default='default_avatar.jpg', upload_to=get_avatar_path)
    last_request_timestamp = models.DateTimeField(_("Last Request Timestamp"), auto_now_add=True)
    enable_2fa = models.BooleanField(_("Enable 2FA"), default=False)

    def __str__(self):
        return self.user.username
