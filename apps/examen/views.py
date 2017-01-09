from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from apps.examen.forms import ExamenForm
from apps.examen.models import Examen


class ExamenListView(ListView):
    model = Examen
    template_name = 'examen/examen_list.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(ExamenListView, self).get_context_data(**kwargs)
        context['form_title'] = u'Examenes'
        return context

class ExamenCreateView(CreateView):
    model = Examen
    form_class = ExamenForm
    template_name = 'examen/examen_form.html'
    success_url = reverse_lazy('examen:examen_list')

    def get_context_data(self, **kwargs):
        context = super(ExamenCreateView, self).get_context_data(**kwargs)
        context['action_title'] = 'Crear'
        context['form_title'] = self.model._meta.verbose_name
        print(Examen._meta.verbose_name_plural)
        print('inggreso')
        return context