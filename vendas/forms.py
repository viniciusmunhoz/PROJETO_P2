from django import forms
from vendas.models import Vendas


class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['calcado', 'quantidade', 'cliente', 'funcionario', 'datavenda', 'loja']
