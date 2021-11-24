from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms


def index(request):
    """
    Página index responsavél por apresentar o formulário
    """
    # Passando por contexto os dados vindo do forms.py para o formulário ser renderizado
    form = PassagemForms()
    pessoa_form = PessoaForms()
    context = {
        'form': form,
        'pessoa_form': pessoa_form
    }
    return render(request, 'index.html', context)


def revisao_consulta(request):
    """
    Página de revisão da consulta feita no formulário
    """

    if request.method == "POST":
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)

        # Verificando se o formulário está validado.
        if form.is_valid():
            # Passando por contexto os dados resgatados do formulário da página index
            context = {'form': form, 'pessoa_form': pessoa_form}
            return render(request, 'minha_consulta.html', context)
        else:
            context = {'form': form, 'pessoa_form': pessoa_form}
            return render(request, 'index.html', context)
