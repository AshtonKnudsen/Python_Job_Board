from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^LoadPage$', views.LoadPage),
    url(r'^new$', views.new),
    url(r'^process$', views.process_new),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^process_edit/(?P<id>\d+)$', views.process_edit),
]