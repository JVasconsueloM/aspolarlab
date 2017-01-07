from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BaseAdmin(TemplateView):
    template_name = 'utils/admin/base.html'