from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from accounts.models import User
from .forms import ConsultaForm
from .models import Consulta
from .models import Paciente
from .forms import PacienteForm


class PacienteList(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    paginate_by = 10



class RelatPacienteList(ListView):
    model = Paciente
    template_name = 'relatorio_paciente_list.html'
    paginate_by = 10



class PacienteCreate(CreateView):
    model = Paciente
    template_name = 'paciente_form.html'
    form_class = PacienteForm


def paciente_detail(request, pk):
    template_name = 'paciente_detail.html'
    obj = Paciente.objects.get(pk=pk)
    object = Consulta.objects.filter(paciente=obj)
    meu_perfil = User.objects.all()
    context = {
        'object': obj,
        'object_list': object,
        'perfil': meu_perfil

    }
    return render(request, template_name, context)



class PacienteUpdate(UpdateView):
    model = Paciente
    template_name = 'paciente_form.html'
    form_class = PacienteForm


class Upload(CreateView):
    model = Paciente
    template_name = 'paciente_form.html'
    form_class = PacienteForm


# CONSULTAS


class ConsultaCreate(CreateView):
    model = Consulta
    template_name = 'paciente_form.html'
    form_class = ConsultaForm


class ConsultaList(ListView):
    model = Paciente
    template_name = 'consulta_list.html'
    paginate_by = 10