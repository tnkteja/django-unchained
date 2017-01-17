from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

from rest_framework import routers

from csc510project import views

restrouter = routers.DefaultRouter()
restrouter.register(r'movies', views.MovieViewSet)
restrouter.register(r'users', views.UserViewSet)
restrouter.register(r"critics", views.CriticViewSet)
from django.views.generic.base import TemplateView
from csc510project.views import AccountViewSet, ExtendedAccountViewSet, MoviePublicViewSet

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^api/authentication',views.authentication),
    url(r'^api/logout',views.logout),
    url(r'^api/register', AccountViewSet.as_view({ "post": "register"})),
    url(r"^api/activate", AccountViewSet.as_view({ "get": "activate"})),
    url(r'^api/account/become_critic', ExtendedAccountViewSet.as_view({ "put": "become_critic"})),
    url(r'^api/account/change_password', AccountViewSet.as_view({ "post": "change_password"})),
    url(r'^api/account/reset_password/init', AccountViewSet.as_view({ "post": "reset_password_init"})),
    url(r'^api/account/reset_password/finish', AccountViewSet.as_view({ "post": "reset_password_finish"})),
    url(r'^api/account', AccountViewSet.as_view({ "get" : "get", "post": "update" })),
    url(r"^api/movies/public",MoviePublicViewSet.as_view({"get": "list"})),
    url(r"^api/_search/movies", include('haystack.urls')),
    url(r'^api/',include(restrouter.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
]
