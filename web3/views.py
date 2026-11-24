from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def mislibros(request):
    return render(request, 'mislibros.html')

def generos(request):
    return render(request, 'generos.html')

def recomendados(request):
    return render(request, 'recomendados.html')