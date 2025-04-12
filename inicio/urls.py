from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name="inicio"),
    path('crear', views.crear_evento, name='crear'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)