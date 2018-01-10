from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.device_table, name='device_table'),
    url(r'^new/$', views.device_new, name ='device_new'),
    url(r'^_delete/(?P<pk>\d+)/$', views.device_delete,
        name='device_delete'),
]
