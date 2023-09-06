from django.db import models

class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=8)
    marca = models.CharField('Marca', max_length=15)
    veiculo = models.CharField('Veículo', max_length=30)
    km_troca_oleo = models.DecimalField('km_Troca_Oleo', max_digits=8, decimal_places=4)
