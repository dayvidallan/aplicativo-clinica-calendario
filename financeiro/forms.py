from django.forms import ModelForm
from .models import Financeiro
from accounts.models import User






class FinanceiroForm(ModelForm):

        class Meta:
            model = Financeiro
            fields = 'profissional', 'paciente', 'servico', 'data', 'valor', 'observacao', 'recibo'









