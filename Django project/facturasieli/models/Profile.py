# facturasieli/models/Profile.py
from django.contrib.auth.models import User
from django.db import models

from facturasieli.models.utils import get_avatar_path


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.jpg', upload_to=get_avatar_path)
    last_request_timestamp = models.DateTimeField(db_default=models.functions.Now())
    enable_2fa = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
