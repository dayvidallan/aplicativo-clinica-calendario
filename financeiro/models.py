from django.db import models
from django.urls import reverse_lazy
from pacientes.models import Paciente
from accounts.models import User
from django.utils import timezone
from django.db.models import Sum



class Procedimento(models.Model):
    profissional = models.ForeignKey(User, on_delete=models.CASCADE)
    procedimeto = models.CharField(max_length=100)
    custo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Custo Médio R$')


    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('financeiro_list')

    def __str__(self):
        return self.procedimeto



class Financeiro(models.Model):
    profissional = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE, blank=True, null=True)
    servico = models.CharField(max_length=100, unique=False)
    data = models.DateTimeField(default=timezone.now)
    valor = models.CharField(max_length=11, blank=True, null=True, verbose_name='R$ Valor')
    observacao = models.TextField(null=True, blank=True)
    recibo = models.BooleanField(verbose_name='Gerar Recibo?', default=False)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('financeiro_list')

    @property
    def total_faturamento(self):

        total = Financeiro.objects.all().aggregate(Sum("valor"))["valor__sum"]

        return total or 0



