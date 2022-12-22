from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    nome = 'Alfredo'
    sexo = 'M'
    lista = [
        {'nome' : 'Pedro', 'sexo': 'M'},
        {'nome' : 'Paulo', 'sexo': 'm'},
        {'nome' : 'Luana', 'sexo': 'F'},
        {'nome' : 'Flavia', 'sexo': 'F'},
    ]

    data = {'sexo': sexo, 'nome': nome, 'lista' : lista}
    return render(request, 'index.html', data)