from collections import UserList
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionManager,
    PermissionsMixin,
)
from django.contrib.auth.hashers import make_password
import jwt


# class Owner(models.Model):
#     name = models.CharField(max_length=55)
#     surname = models.CharField(max_length=55)
#     number = models.IntegerField(blank=True, null=True,default='')
#     def __str__(self):
#         return self.name


class Pets(models.Model):
    # owner = models.ManyToManyField(Owner, default='')
    pets_name = models.CharField(max_length=55)
    content = models.TextField()
    # photo = models.ImageField(upload_to='sultan/static/photo/', blank=True)

    def __str__(self):
        return self.pets_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
