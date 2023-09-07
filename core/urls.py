from django.urls import path
from .views import index, veiculo, motorista, aluguel, aluguel_edit, aluguel_view, aluguel_delete

urlpatterns = [
    path('', index, name='index'),
    path('veiculo', veiculo, name='veiculo'),
    path('motorista', motorista, name='motorista'),
    path('aluguel', aluguel, name='aluguel'),
    path('aluguel_edit/<int:id>', aluguel_edit, name='aluguel_edit'),
    path('aluguel_view/<int:id>', aluguel_view, name='aluguel_view'),
    path('aluguel_delete/<int:id>', aluguel_delete, name='aluguel_delete')
]
