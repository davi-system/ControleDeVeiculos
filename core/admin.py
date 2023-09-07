from django.contrib import admin
from .models import Veiculo, Motorista, Aluguel

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'veiculo', 'km_troca_oleo')

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cnh')

@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'motorista', 'data_saida', 'hora_saida', 'km_saida', 'destino', 'data_retorno', 'hora_retorno', 'km_retorno', 'km_percorrido')
