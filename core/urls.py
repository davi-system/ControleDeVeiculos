from django.urls import path
from .views import index, veiculo, motorista

urlpatterns = [
    path('', index, name='index'),
    path('veiculo', veiculo, name='veiculo'),
    path('motorista', motorista, name='motorista')
]
