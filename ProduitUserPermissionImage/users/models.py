
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    #is_admin = models.BooleanField('Is Stock Manager', default = False)
    #is_stockManager = models.BooleanField('Is Admin', default = False)
    #is_storeKeeper = models.BooleanField('Is Store Keeper', default = False)
    #is_guest = models.BooleanField('Is Guest', default = False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
