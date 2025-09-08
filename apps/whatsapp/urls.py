from django.urls import path
from . import views

app_name = 'whatsapp'

urlpatterns = [
    path('enviar/', views.enviar_mensaje_whatsapp, name='enviar_mensaje'),
]