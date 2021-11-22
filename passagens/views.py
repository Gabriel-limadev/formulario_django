from django.shortcuts import render
from passagens.forms import PassagemForms

def index(request):
    """
    Página index responsavél por apresentar o formulário
    """
    # Passando por contexto os dados vindo do forms.py para o formulário ser renderizado
    form = PassagemForms()
    context = {
        'form' : form
    }
    return render(request, 'index.html', context)

def revisao_consulta(request):
    """
    Página de revisão da consulta feita no formulário
    """

    if request.method == "POST":
        form = PassagemForms(request.POST)
        # Passando por contexto os dados resgatados do formulário da página index
        context = {
            'form' : form
        }   
    return render(request, 'minha_consulta.html', context)