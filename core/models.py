from django.db import models


class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=8)
    marca = models.CharField('Marca', max_length=15)
    veiculo = models.CharField('Veículo', max_length=30)
    km_troca_oleo = models.DecimalField('km_Troca_Oleo', max_digits=8, decimal_places=4)

    def __str__(self):
        return self.marca


class Motorista(models.Model):
    nome = models.CharField('Nome', max_length=50)
    telefone = models.CharField('Telefone', max_length=10)
    cnh = models.IntegerField('CNH')

    def __str__(self):
        return self.nome


class Aluguel(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    data_saida = models.DateField('Data_saida')
    hora_saida = models.TimeField('Hora_saida')
    km_saida = models.DecimalField('Km_saida', max_digits=8, decimal_places=4)
    destino = models.CharField('Destino', max_length=100)
    data_retorno = models.DateField('Data_retorno')
    hora_retorno = models.TimeField('Hora_retorno')
    km_retorno = models.DecimalField('Km_retorno', max_digits=8, decimal_places=4)
    km_percorrido = models.DecimalField('Km_percorrido', max_digits=8, decimal_places=4)
