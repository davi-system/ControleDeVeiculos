from django import forms
from .models import Veiculo

class VeiculoFormModel(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'marca', 'veiculo', 'km_troca_oleo']