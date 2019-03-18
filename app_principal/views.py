from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Livro
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import FiltroGenero
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from app_principal.forms import CadastroForm
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# Create your views here.

class ExibirLivro(ListView):
    model = Livro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FiltroGenero(self.request.GET, queryset=self.get_queryset())
        return context

def pagina_inicial(request):
    return render(request, 'index.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_staff = True
            #update_permission(user)
            user.groups.add(1)
            user.save()
            login(request, user)
            return redirect('/')
    
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

