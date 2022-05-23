from django.forms import ModelForm
from django import forms
from .models import Financeiro
from accounts.models import User






class FinanceiroForm(forms.ModelForm):
        def __init__(self, user, *args, **kwargs):
            super(FinanceiroForm, self).__init__(*args, **kwargs)
            self.fields['profissional'].queryset = User.objects.filter(
                email=user)

        class Meta:
            model = Financeiro

            fields = 'profissional', 'paciente', 'servico', 'data', 'valor', 'observacao', 'recibo'





                













