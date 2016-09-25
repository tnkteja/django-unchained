from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

from rest_framework import routers

from csc510project import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
from django.views.generic.base import TemplateView
urlpatterns = [
 url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^api/',include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
