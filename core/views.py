from django.shortcuts import render
from .forms import VeiculoFormModel, MotoristaFormModel
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def veiculo(request):
    if str(request.method) == 'POST':
        form = VeiculoFormModel(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')

            form = VeiculoFormModel()
        else:
            messages.error(request, 'Algo deu errado!')
    else:
        form = VeiculoFormModel()
    context = {
        'form': form
    }
    return render(request, 'veiculo.html', context)


def motorista(request):
    if str(request.method) == 'POST':
        form = MotoristaFormModel(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')

            form = MotoristaFormModel()
        else:
            messages.error(request, 'Algo deu errado!')
    else:
        form = MotoristaFormModel()
    context = {
        'form': form
    }
    return render(request, 'motorista.html', context)
