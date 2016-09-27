from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from .models import Movie
from django.contrib.auth.models import User
from .serializers import MovieSerializer, UserSerializer
from django.contrib.auth import authenticate, login, logout as Logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import logging
from django.views.decorators.csrf import ensure_csrf_cookie
import json
# Create your views here.

logger = logging.Logger("django")

def index(request):
    # return HttpResponse('Hello from Python!')
    logger.debug(request)
    return render_to_response(request, 'index.html')

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


def authentication(request):
	print request.POST
	user = authenticate(username=request.POST["j_username"],password=request.POST["j_password"])
	print user
	if user:
		login(request, user)
		return HttpResponse()
	return HttpResponseBadRequest()

def logout(request):
	print request.session
	Logout(request)
	return HttpResponse()

@api_view(http_method_names=['GET'])
def account(request):
	print request.user.__dict__
	return Response(json.dumps(request.user.__dict__))