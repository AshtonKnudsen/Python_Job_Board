from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg$', views.reg),
    url(r'^good$', views.good),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]