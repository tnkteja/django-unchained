from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from rest_framework import viewsets
from .models import Movie, Critic
from django.contrib.auth.models import User
from .serializers import MovieSerializer, UserSerializer, CriticSerializer
from django.contrib.auth import authenticate, login, logout as Logout
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import logging
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import UserSerializer
import json
# Create your views here.

logger = logging.getLogger("django")

def index(request):
    # return HttpResponse('Hello from Python!')
    logger.debug(request)
    return render_to_response(request, 'index.html')

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CriticViewSet(viewsets.ModelViewSet):
    queryset = Critic.objects.all()
    serializer_class = CriticSerializer

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

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

def account(request):
    """
    Note: Django provides a "login_required" decorator but it need a rediret login url
    incase of failure, therfore not using it.
    """
    return JsonResponse({
        "firstNname": request.user.first_name,
        "lastName": request.user.last_name, 
        "email": request.user.email,
        "roles":request.user.extendedUser.roles
        }) if request.user.is_authenticated else HttpResponseUnauthorized()

from rest_framework.status import HTTP_200_OK
from json import loads

class AccountViewSet(viewsets.ViewSet):
    def get(self, request):
        user=User.objects.get(username=request.user.get_username())
        print user.username
        return JsonResponse({
            "first_name": user.first_name,
            "last_name": user.last_name, 
            "email": user.email,
            "roles": user.extendeduser.roles
            }) if request.user.is_authenticated else HttpResponseUnauthorized()

    def update(self,request, *args, **kwargs):
        try:
            user=User.objects.get(id=request.user.id)
            user.first_name=request.data["first_name"]
            user.last_name=request.data["last_name"]
            user.email=request.data["email"]
            user.save()
            return Response(status= HTTP_200_OK)
        except Exception as e:
            return HttpResponseBadRequest(e)

    def change_password(self, request, *args, **kwargs):
        try:
            user=User.objects.get(id=request.user.id)
            user.set_password(self.request.data["new_password"])
            user.save()
            return Response(status= HTTP_200_OK)
        except Exception as e:
            return HttpResponseBadRequest(e)

    def register(self, request):
        try:
            if User.objects.get(username=request.data["username"]):
                return HttpResponseBadRequest("Username already exists")
            u=User.create_user(request.data["username"], email=request.data["email"], password=request.data["password"])
            u.extendeduser=Extendeduser()
            u.extendeduser.roles=dumps(["ROLE_USER"])
            u.save()
        except Exception as e:
            return HttpResponseBadRequest(e)

class ExtendedAccountViewSet(viewsets.ViewSet):

    def become_critic(self, request):
        try:
            return HttpResponse()
        except Exception as e:
            return HttpResponseBadRequest(e)

