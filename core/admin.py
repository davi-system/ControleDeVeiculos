from django.contrib import admin
from .models import Veiculo, Motorista

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'veiculo', 'km_troca_oleo')

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cnh')
