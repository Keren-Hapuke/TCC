from django.shortcuts import render

def index(request):
    return render(request)

def relatorio(request):
    return render(request, 'relatorio.html')
