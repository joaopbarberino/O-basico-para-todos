from django.contrib import admin
from .models import Livro


admin.site.site_header = "O básico para todos"
admin.site.title = "Clique" 

admin.site.register(Livro)
