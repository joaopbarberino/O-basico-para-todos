from django.shortcuts import render

# Create your views here.

def SOCORRO(request):
    teste = 'teste'
    return render(request, 'index.html', {'teste' : teste})