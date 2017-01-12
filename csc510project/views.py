#!/usr/bi/python

from hashlib import md5
from json import loads, dumps
import logging

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
from django.contrib.auth import authenticate, login, logout as Logout
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
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
    if user and user.is_active:
        login(request, user)
        return HttpResponse()
    return HttpResponseBadRequest()

def logout(request):
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


class AccountViewSet(viewsets.ViewSet):
    def get(self, request):
        print request.user.username
        return JsonResponse({
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "roles": loads(request.user.extendeduser.roles)
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
        try:
            try:
                User.objects.get(username=request.data["username"])
                return HttpResponseBadRequest("Username already exists")
            except User.DoesNotExist as e:
                u=User.create_user(request.data["username"], email=request.data["email"], password=request.data["password"])
                u.extendeduser=Extendeduser()
                u.extendeduser.roles=dumps(["ROLE_USER"])
                m=md5()
                m.update(u.username+u.email)
                u.extendeduser.activationkey=m.digest()
                u.extendeduser.save()
                u.is_active = False
                u.save()
                send_mail("Activate",self.__class__.mail_template%(u.username,'',u.extendeduser.activationkey,"admin."), "csc510project@gmail.com", [u.email])
                return HttpResponse()
        except Exception as e:
            return HttpResponseBadRequest(e)

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
            eu=ExtendedUser.objects.get(activationkey=self.request.data["key"])
            eu.user.is_active=True
            return HttpResponse()
        except Exception as e:
            return HttpResponseBadRequest(e)

    def reset_begin(self, request, *args, **kwargs):
        pass

    def reset_end(self, request, *args, **kwargs):
        pass


class ExtendedAccountViewSet(viewsets.ViewSet):

    def become_critic(self, request):
        try:
            return HttpResponse()
        except Exception as e:
            return HttpResponseBadRequest(e)


class MoviePublicViewSet(viewsets.ModelViewSet):
    class CustomPaginationClass(PageNumberPagination):
        #page_query_param="page" # "page" is default
        page_size=10
        page_size_query_param="size"
        max_page_size=50
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = CustomPaginationClass