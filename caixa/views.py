from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import CX_Filter
from .forms import *
from .models import CC, Conta, Pessoa
from dal import autocomplete
import json
import pandas as pd
import numpy as np
import openpyxl
from datetime import datetime
from decimal import *
from .models import CC, Conta


def cx_list(request):
    pass


def import_conta():
    df = pd.read_csv (r'c:\dados2.csv', delimiter=';')

    ct_list = df['CONTA'].unique()
    for ct in ct_list:
        print(ct)
        conta = Conta()
        conta.conta = ct
        conta.save()

    #print(ct)
    #for index, row in df.iterrows():
    # print(row["DESC"])


def import_dados():
    df = pd.read_csv (r'c:\dados2.csv', delimiter=';')

    cc = CC.objects.all().delete()
    for index, row in df.iterrows():
        conta = Conta.objects.filter(conta=row['CONTA'])
        data  = datetime.strptime(row['DATA'], '%d/%m/%Y')
        credito = Decimal(row['CREDITO'].replace(',', '.'))
        debito = Decimal(row['DEBITO'].replace(',', '.'))
        cc = CC()
        cc.data = data
        cc.desc = row['DESC']
        cc.banco = row['BANCO']
        cc.conta = conta[0]
        cc.credito = credito
        cc.debito = debito
        cc.save()


def to_pandas():
    df = pd.DataFrame(list(CC.objects.all().values('conta__conta', 'banco', 'credito', 'debito' )))
    print(df)

    table = pd.pivot_table(df, index=['conta__conta'], aggfunc={'credito': np.sum, 'debito': np.sum})
    print(table)
    table.to_excel("c:\django\output4.xlsx") 
    #table.to_csv('c:\django\output.csv', sep=';') 



#import_conta()
#import_dados()
#to_pandas()









class ParcAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        print('nome-autocomplete')
        if not self.request.user.is_authenticated:
            return Pessoa.objects.none()
        qs = Pessoa.objects.only('nome')
        if self.q:
            qs = qs.filter(nome__icontains=self.q)
        return qs


class ContaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        print('conta-autocomplete')
        if not self.request.user.is_authenticated:
            return Pessoa.objects.none()
        qs = Conta.objects.only('conta')
        if self.q:
            qs = qs.filter(conta__icontains=self.q)
        return qs


def cx_list(request):
    lista = CX_Filter(request.GET, queryset=CC.objects.all().order_by('-data'))
    paginator = Paginator(lista.qs, 20) # Show 25 contacts per page.
    page_number = request.GET.get('page', 1)

    lote = CX_acoes_lote_form()

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'caixa/cx_list.html', {'page_obj': page_obj, 'lista': lista, 'lote': lote})



def cx_filter(request):

    lista = CC.objects.all().order_by('-data')
    paginator = Paginator(lista, 20) # Show 25 contacts per page.
    
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'caixa/cx_list.html', {'page_obj': page_obj })

def cx_lote(request):

    chkeds = request.POST.get('chkeds')
    opt = request.POST.get('opt')
    print("Estes são os selecionados", chkeds, " com esta opcao: ", opt )

    dict = {'ret': "oi"}
    return HttpResponse(json.dumps(dict), content_type='application/json')



def cx_detail(request, pk):
    cx = get_object_or_404(CC, pk=pk)
    if request.method == 'POST':
        #print(request.POST)
        act = request.POST['act']

        if act == 'delete':
            cx.delete()
            form = CX_detail_form()
            return redirect('caixa:cx_list')
        elif act == 'save':
            print('act=save')
            form = CX_detail_form(request.POST, instance = cx)
            if form.is_valid():
                print('form is valid')
                #form = ProdDetailForm(form.cleaned_data)
                form.save()
            return redirect('/caixa/new')
    else:
        form = CX_detail_form(instance=cx)
        return render(request, 'caixa/cx_detail.html', {'form': form, 'inst_id':pk})


def cx_new(request):
    if request.method == 'POST':
        form = CX_detail_form(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
            return redirect('caixa:cx_detail', pk=inst.pk)
        else:
            return render(request, 'caixa/cx_detail.html', {'form': form})
    else:
        form = CX_detail_form()
        return render(request, 'caixa/cx_detail.html', {'form': form})


