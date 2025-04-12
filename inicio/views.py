from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Evento
def listar_eventos(request):
    evento = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'evento': evento})


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)  # Incluir request.FILES para manejar archivos
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')  # Redirige a la lista de eventos
    else:
        form = EventoForm()

    return render(request, 'inicio.html', {'form': form})