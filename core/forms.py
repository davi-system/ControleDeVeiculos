from django import forms
from .models import Veiculo, Motorista, Aluguel

class VeiculoFormModel(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'marca', 'veiculo', 'km_troca_oleo']


class MotoristaFormModel(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nome', 'telefone', 'cnh']


class AluguelFormModel(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['veiculo', 'motorista', 'data_saida', 'hora_saida', 'km_saida', 'destino', 'data_retorno', 'hora_retorno', 'km_retorno', 'km_percorrido']
