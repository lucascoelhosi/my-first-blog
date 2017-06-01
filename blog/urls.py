# Importações de Views para as URLS

from django.conf.urls import include, url 
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
]
