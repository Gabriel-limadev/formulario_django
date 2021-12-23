from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.class_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(
        label='Data de pesquisa',
        disabled=True,
        initial=datetime.today)

    class Meta:

        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida',
                  'data_volta': 'Data de volta', 'informacoes': 'Informações', 'classe_viagem': 'Classe da Viagem'}

        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }

    def clean(self):
        """[Metodo de validação de campos do formulário]

        Returns:
            [lista_erros]: [Os erros de cada validação]
        """
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_hoje = self.cleaned_data.get('data_pesquisa')

        lista_erros = {}

        campo_com_numero(origem, 'origem', lista_erros)
        campo_com_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        data_ida_maior_data_volta(data_ida, data_volta, lista_erros)
        data_ida_menor_data_hoje(data_ida, data_hoje, lista_erros)

        # Verificando se a lista de erros está vazia, caso não a mensagem de erro será adicionada.
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_error = lista_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        # fields = ['email'] -> Traz o campo email
        exclude = ['nome']  # traz todos os campos menos o nome
