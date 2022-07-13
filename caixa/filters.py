from .models import *
import django_filters
from django_filters import CharFilter

class CX_Filter(django_filters.FilterSet):
    pessoa = CharFilter(field_name='pessoa__nome', lookup_expr='icontains', label='Nome')
    conta = django_filters.CharFilter(field_name='conta__conta', lookup_expr='icontains', label='conta')
    cidade = django_filters.CharFilter(field_name='parceiro__cidade', lookup_expr='icontains', label='parceiro')
    desc = django_filters.CharFilter(field_name='desc', lookup_expr='icontains', label='Descrição')
    data__gte = django_filters.DateFilter(field_name='data', lookup_expr='gte', label='Data, a partir de:')
    data__lte = django_filters.DateFilter(field_name='data', lookup_expr='lte', label='Data, até:')

    class Meta:
        model = CC

        fields = {
            'banco':['exact']
            }
