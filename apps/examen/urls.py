from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^examen/$', ExamenListView.as_view(), name='examen_list'),
    url(r'^examen/nuevo/$', ExamenCreateView.as_view(), name='examen_create'),
]