from django.contrib import admin

# Register your models here.
from .models import Movie, Critic
admin.site.register(Movie)
admin.site.register(Critic)