#!/usr/bi/python
from __future__ import unicode_literals

from base64 import b64encode
from hashlib import md5
from json import loads, dumps
import logging
from time import time

from django.contrib.auth import authenticate, login, logout as Logout
from django.contrib.auth.models import User
from django.core import serializers
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets

from .models import Movie, Critic, ExtendedUser
from django.contrib.auth.models import User
from .serializers import MovieSerializer, UserSerializer, CriticSerializer
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework import status
import logging
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import UserSerializer
from json import dumps, loads
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
    user = authenticate(username=request.POST["j_username"],password=request.POST["j_password"])
    if user:
        login(request, user)
        return HttpResponse()
    return HttpResponseBadRequest()

def logout(request):
    logout(request)
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

def create_extendeduser(backend, user, response, *args, **kwargs):
    if not hasattr(user, "extendeduser"):
        user.extendeduser=ExtendedUser()
        user.extendeduser.roles=dumps(["ROLE_USER"])
        user.extendeduser.save()
    #user.email_user("Account Created","", "csc510project@gmail.com", fail_silently=False)

class AccountViewSet(viewsets.ViewSet):
    def get(self, request):
        print request.user.username
        return JsonResponse({
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "authorities": loads(request.user.extendeduser.roles)
            }) if request.user.is_authenticated else HttpResponseUnauthorized()

    def update(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseUnauthorized()
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
        # try:
        try:
            User.objects.get(username=request.data["username"])
            return HttpResponseBadRequest("Username already exists")
        except User.DoesNotExist as e:
            u=User.objects.create_user(request.data["username"], email=request.data["email"], password=request.data["password"])
            u.extendeduser=ExtendedUser()
            u.extendeduser.roles=dumps(["ROLE_USER"])
            m=md5()
            m.update(u.username+u.email)
            u.extendeduser.activationkey=b64encode(m.digest())
            u.extendeduser.save()
            u.is_active = False
            u.save()
            send_mail("Activate",u.extendeduser.activationkey, "csc510project@gmail.com", [u.email], fail_silently=False)
            return HttpResponse()
        # except Exception as e:
        #     return HttpResponseBadRequest(e)

    mail_template = \
    """
    <!DOCTYPE html>
    <html xmlns:th="http://www.thymeleaf.org">
        <head>
            <title>JHipster activation</title>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        </head>
        <body>
            <p>
                Dear %s,
            </p>
            <p>
                Your %s account has been created, please click on the URL below to activate it:
            </p>
            <p>
                <a href="/#/activate?key=%s">Activation Link</a>
            </p>
            <p>
                <span>Regards, </span>
                <br/>
                <em>%s.</em>
            </p>
        </body>
    </html>
    """

    def activate(self, request, *args, **kwargs):
        try:
            eu=ExtendedUser.objects.get(activationkey=request.GET["key"])
            if eu.user.is_active:
                return HttpResponseBadRequest("User already activated.")
            eu.user.is_active=True
            eu.user.save()
            return HttpResponse()
        except Exception as e:
            return HttpResponseBadRequest(e)

    def reset_password_init(self, request, *args, **kwargs):
        try:
            u=User.objects.get(email=request.POST["email"])[0]
            m=md5()
            m.update(u.username+u.email+time())
            u.extendeduser.resetkey=b64encode(m.digest())
            u.extendeduserresetkeyexpirytime = time() + 86400
            u.extendeduser.save()
            u.email_user("Reset Password",u.extendeduser.resetkey, "csc510project@gmail.com", fail_silently=False)
            return HttpResponse()
        except User.DoesNotExist as e:
            HttpResponseBadRequest("e-mail address not registered")
        except Exception as e:
            return HttpResponseBadRequest(e)

    def reset_password_finish(self, request, *args, **kwargs):
        try:
            eu=ExtendedUser.objects.get(resetkey=request.POST["key"])
            if time() > eu.resetkeyexpirytime:
                eu.user.set_password(request.POST("new_password"))
                eu.user.save()
                return HttpResponse()
            return HttpResponseBadRequest("Reset Key Expired")
        except Exception as e:
            return HttpResponseBadRequest(e)


class ExtendedAccountViewSet(viewsets.ViewSet):

    def become_critic(self, request):
        try:
            return HttpResponse()
        except Exception as e:
            return HttpResponseBadRequest(e)
