from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from accounts.models import User
from .models import Procedimento
from .models import Financeiro
from .forms import FinanceiroForm



class ReciboList(ListView):
    model = Financeiro
    template_name = 'financeiro_list.html'





class ReciboCreate(CreateView):
    model = Financeiro
    template_name = 'recibo_form.html'
    form_class = FinanceiroForm



def recibo_detail(request, pk):
    template_name = 'recibo_detail.html'
    obj = Financeiro.objects.get(pk=pk)
    context = {
        'object': obj,


    }
    return render(request, template_name, context)



def recibo_add(request):
    form = FinanceiroForm(request.POST or None)
    template_name = 'financeiro_list.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('financeiro_list'))

    context = {'form': form}
    return render(request, template_name, context)


class ReciboUpdate(UpdateView):
    model = Financeiro
    template_name = 'recibo_form.html'
    form_class = FinanceiroForm




#RELATORIO

class RelatorioList(ListView):
    model = Financeiro
    template_name = 'relatorio_list.html'




#PROCEDIMENTOS

