from django.forms import ModelForm
from .models import Financeiro







class FinanceiroForm(ModelForm):


        class Meta:
            model = Financeiro
            fields = 'profissional', 'paciente', 'servico', 'data', 'valor', 'observacao', 'recibo'






