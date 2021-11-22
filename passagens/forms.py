from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import date

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')

class PassagemForms(forms.Form):
    origem     = forms.CharField(label='Origem', max_length=100)
    destino    = forms.CharField(label='destino', max_length=100)
    data_ida   = forms.DateField(
        label='Ida',
        widget=DatePicker(
            options={
                'minDate': '2020-01-01',
                'maxDate': '2030-12-31',
            },
        ),
        initial=data_em_texto)
    data_volta = forms.DateField(
        label='Volta', 
        widget=DatePicker(
            options={
                'minDate': '2020-01-01',
                'maxDate': '2030-12-31',
            },
        ), 
        initial=data_em_texto)