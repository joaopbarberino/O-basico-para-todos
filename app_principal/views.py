from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Livro
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import FiltroGenero

# Create your views here.

class ExibirLivro(ListView):
    model = Livro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FiltroGenero(self.request.GET, queryset=self.get_queryset())
        return context