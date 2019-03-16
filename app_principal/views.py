from django.shortcuts import render
from app_principal.models import Livro

# Create your views here.

def SOCORRO(request):
    livros = Livro.objects.all()
    
    contexto = {
        'livros': livros
    }

    return render(request, 'index.html', contexto)