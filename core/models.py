from django.db import models

class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=8)
    marca = models.CharField('Marca', max_length=15)
    veiculo = models.CharField('Veículo', max_length=30)
    km_troca_oleo = models.DecimalField('km_Troca_Oleo', max_digits=8, decimal_places=4)


class Motorista(models.Model):
    nome = models.CharField('Nome', max_length=50)
    telefone = models.CharField('Telefone', max_length=10)
    cnh = models.IntegerField('CNH', max_length=10)
