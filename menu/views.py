from django.shortcuts import render
from django.http import HttpResponse
# Vista para la página principal
def index(request):
    title = 'Sistema Contable'
    return render(request, 'index.html',{
        'title': title
    })

def login(request):
    return render(request, 'login.html')

def sistema(request):
    return render(request, 'sistema.html')
