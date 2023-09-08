from django.shortcuts import render, redirect, get_object_or_404
from .forms import VeiculoFormModel, MotoristaFormModel, AluguelFormModel
from .models import Aluguel
from django.contrib import messages


def index(request):
    aluguel = Aluguel.objects.order_by('-data_saida')
    data_saida_pesquisa = request.GET.get('data_saida')

    if data_saida_pesquisa:
        aluguel = Aluguel.objects.filter(data_saida=data_saida_pesquisa)

    context = {
        'aluguel': aluguel
    }
    return render(request, 'index.html', context)


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


def aluguel(request):
    if str(request.method) == 'POST':
        form = AluguelFormModel(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')

            form = AluguelFormModel()
        else:
            messages.error(request, 'Algo deu errado!')
    else:
        form = AluguelFormModel()
    context = {
        'form': form
    }
    return render(request, 'aluguel.html', context)


def aluguel_edit(request, id):
    aluguel = get_object_or_404(Aluguel, id=id)
    form = AluguelFormModel(instance=aluguel)
    context = {
        'aluguel': aluguel,
        'form': form
    }
    if str(request.method) == 'POST':
        form = AluguelFormModel(request.POST, instance=aluguel)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'aluguel_edit.html', context)
    else:
        return render(request, 'aluguel_edit.html', context)


def aluguel_view(request, id):
    form = get_object_or_404(Aluguel, id=id)
    context = {
        'form': form
    }
    return render(request, 'aluguel_view.html', context)


def aluguel_delete(request, id):
    aluguel = get_object_or_404(Aluguel, id=id)
    aluguel.delete()
    return redirect('index')
