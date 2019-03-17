import django_filters
from .models import Livro

class FiltroGenero(django_filters.FilterSet):

    genero = django_filters.ChoiceFilter(choices = Livro.genero_opcoes)
    class Meta:
        model = Livro
        fields = {
            'nome': ['icontains'], 
            'autor': ['icontains']
        }