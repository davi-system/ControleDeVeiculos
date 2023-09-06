from django import forms
from .models import Veiculo, Motorista

class VeiculoFormModel(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'marca', 'veiculo', 'km_troca_oleo']

class MotoristaFormModel(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nome', 'telefone', 'cnh']
