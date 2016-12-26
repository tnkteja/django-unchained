from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import *

# Create your models here.
class Movie(Model):
	name=CharField(max_length=255)
	description=TextField()
	image=CharField(max_length=255)

class Critic(Model):
	user= OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
	isActive=BooleanField()

class ExtendedUser(Model):
	user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
	activationkey = CharField(max_length=255, unique=True)
	resetkey = CharField(max_length=255)
	resetkeyexpirytime = IntegerField(default=0)
	roles = CharField(max_length=255)
	primaryemail = CharField(max_length=255, unique=True, default="")
