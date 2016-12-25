#!/usr/bin/python

from .models import Movie, Critic
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from django.contrib.auth.models import User

class MovieSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('url','name', 'description', 'image')

class CriticSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Critic
		fields = ("user","isActive")

class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = (
			'id',
		 	'username',
		 	"first_name",
		 	"last_name",
		 	"email",
		 	'password',
		 	"groups",
		 	"user_permissions",
		 	"is_staff",
		 	"is_active",
		 	"is_superuser",
		 	"last_login",
		 	"date_joined"
		 	)
