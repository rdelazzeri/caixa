from django.urls import path
from .models import Pessoa
from . import views as v

app_name = 'caixa'

urlpatterns = [
    path('', v.cx_list, name = 'cx_list'),
    path('caixa/list', v.cx_list, name = 'cx_list'),
    path('caixa/filter', v.cx_filter, name = 'cx_filter'),
    path('caixa/lote', v.cx_lote, name = 'cx_lote'),
    path('caixa/new', v.cx_new, name = 'cx_new'),
    path('caixa/detail/<int:pk>', v.cx_detail, name = 'cx_detail'),
    path('parc-autocomplete/', v.ParcAutocomplete.as_view(model=Pessoa, create_field='nome'), name='parc-autocomplete'),
    path('conta-autocomplete/', v.ContaAutocomplete.as_view(), name='conta-autocomplete'),



]