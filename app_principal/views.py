from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Livro
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import FiltroGenero
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from app_principal.forms import CadastroForm, EmailForm
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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

def ajuda(request):
    return render(request, 'ajuda.html')

def contato(request):
    return render(request, 'contato.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_staff = True
            user.groups.add(1)
            user.save()
            login(request, user)
            return redirect('/')
    
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('seu_email')
            mensagem = form.cleaned_data.get('menssagem')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['contato.obasicoparatodos@gmail.com']
            send_mail( usuario, mensagem, email_from, recipient_list )            
            messages.success(request, 'Pronto! Responderemos assim que possível.')
        
    else:
        form = EmailForm()
    return render(request, 'contato.html', {'form': form})