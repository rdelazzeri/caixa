from django import forms
from .models import *
from django.forms import ModelForm, fields, Form
from dal import autocomplete

LOTE_OPCOES = (
    ('0','Ações em lote'),
    ('1','Baixar com data de hoje'),
    ('2','Baixar com data do vencimento'),
    ('3', 'Somar')
)


class CX_detail_form(ModelForm):
    
    #entrada = forms.CharField(max_length=60, label='Nota de entrada', required=False, disabled=False, widget=forms.TextInput(attrs={'size': '60'}))

    class Meta:
        model = CC
        fields = '__all__'
        widgets = {
            'pessoa': autocomplete.ModelSelect2(
                url='caixa:parc-autocomplete',
                attrs={'data-minimum-input-length': 3,
                        'dropdownAutoWidth': True,
                },
                ),          

            'conta': autocomplete.ModelSelect2(
                url='caixa:conta-autocomplete',
                attrs={'data-minimum-input-length': 3,
                        'dropdownAutoWidth': True,
                },
                ),          

        }

class CX_acoes_lote_form(Form):
    opcoes = forms.ChoiceField(choices = LOTE_OPCOES, label="")

