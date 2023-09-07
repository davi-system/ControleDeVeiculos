from django.urls import path
from .views import index, veiculo, motorista, aluguel

urlpatterns = [
    path('', index, name='index'),
    path('veiculo', veiculo, name='veiculo'),
    path('motorista', motorista, name='motorista'),
    path('aluguel', aluguel, name='aluguel')
]
