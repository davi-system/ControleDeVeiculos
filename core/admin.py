from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'veiculo', 'km_troca_oleo')
