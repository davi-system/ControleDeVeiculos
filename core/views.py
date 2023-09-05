from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def veiculo(request):
    return render(request, 'veiculo.html')


def motorista(request):
    return render(request, 'motorista.html')
