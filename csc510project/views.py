from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Movie
from django.contrib.auth.models import User
from .serializers import MovieSerializer, UserSerializer
# Create your views here.

def index(request):
    # return HttpResponse('Hello from Python!')
    return render_to_response(request, 'index.html')

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
