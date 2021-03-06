from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from entregas import views
from entregas.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^Paqueteria/', include('Paqueteria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login',LoginUser.as_view(), name='Login'),
    url(r'^users',include('entregas.urls')),
    url(r'^destinatario',include('entregas.urls')),
)
