from django import forms 
from .models import Eventos

class EventoForm(forms.ModelForm):
    class Meta:
        model = Eventos 
        fields = ['nombre', 'descripcion', 'nomb_org', 'cont_org', 'fecha', 'lugar']