from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroForm(UserCreationForm): 
    nome= forms.CharField(max_length = 30, required = True)
    sobrenome = forms.CharField(max_length = 50, required = True)
    email = forms.EmailField(max_length = 254)
    

    class Meta:
        model = User
        fields = ('username', 'nome', 'sobrenome', 'email', 'password1', 'password2' )

class EmailForm(forms.Form):
    seu_email = forms.EmailField(max_length = 50, required = True)
    mensagem = forms.CharField(widget = forms.Textarea, max_length = 500, required = True)
    fields = ('seu_email', 'mensagem')
    