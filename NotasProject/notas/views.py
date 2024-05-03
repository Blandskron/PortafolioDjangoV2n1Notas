from django.shortcuts import render
from .models import Nota

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})
