#!/usr/bin/python


from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from csc510project.views import *

rr=routers.DefaultRouter()
rr.register(r'critics', CriticViewSet)
rr.register(r'movies', MovieViewSet)
rr.register(r'users', UserViewSet)
