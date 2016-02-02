from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from entregas import views
from .views import *

urlpatterns = patterns('',

	
	url(r'^/logout',LogoutUser.as_view(), name='Logout'),
	url(r'^/verDestinatario',views.verDestinatario, name='verDestinatario'),
	url(r'^/verDestinoDetalle/(?P<destinatario_id>\d+)$',views.verDetalleDesti, name='verDetalleDest'),
	url(r'^/anadirDestinatario',anadirDestinatario.as_view(), name='anadirDestino'),
	url(r'^/registrar',CreateUser.as_view(), name='registro'),
)
