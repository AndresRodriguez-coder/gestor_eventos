from django.shortcuts import render, redirect
from .forms import EventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventoForm()
    return render(request, 'inicio.html', {'form': form})