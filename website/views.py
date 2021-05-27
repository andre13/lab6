#  website/views.py

from django.shortcuts import render
import datetime


def home_page_view(request):
    context = {
        'nome': "André Abreu",
        'agora': datetime.datetime.now(),
    }

    return render(request, 'website/home.html', context)


def sobre_page_view(request):
    listaItens = ["Música", "Guitarra"]
    context = {
        'listaItens': listaItens,
    }
    return render(request, 'website/sobre.html', context)


def contatos_page_view(request):
    context = {
        'morada': "Rua Dom Manuel",
        'contato': "219999999"
    }
    return render(request, 'website/contatos.html', context)