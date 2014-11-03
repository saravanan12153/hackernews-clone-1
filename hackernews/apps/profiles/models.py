from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
