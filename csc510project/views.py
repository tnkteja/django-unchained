from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer