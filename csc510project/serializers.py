from .models import Movie
from rest_framework import serializers
from django.contrib.auth.models import User

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('url','name', 'description', 'image')

class UserSerializer(serializers.ModelSerializer):
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