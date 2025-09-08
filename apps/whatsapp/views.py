import requests
from django.shortcuts import render, redirect
from django.contrib import messages

from config import base
from .forms import EnviarMensajeForm

def enviar_mensaje_whatsapp(request):
    if request.method == 'POST':
        form = EnviarMensajeForm(request.POST)
        
        if form.is_valid():
            numero = form.cleaned_data['numero']

            # URL de la imagen que ya está en tu plantilla de Meta
            STATIC_HEADER_IMAGE_URL = request.build_absolute_uri(base.STATIC_URL + 'images/unityflow_logo.png')
            
            API_URL = "https://graph.facebook.com/v22.0/680742485123092/messages"
            TOKEN = "EAARyZAZBfQm3cBPRNkqPtrAQh67hLjwbHHNZBhmFZBZAaPXG2u6FWfZBibOvIaEAO0KNLh7tN5ADD5fNLYxClUpGja1YsHVFtPZBtV0pKVwFnBjuXcmehuVZBNqHB6vQADJ1VttrTlXW8wVWbr5ZCP3HWFjyNjdhYkaKhJ6ZAX5mhaLiB512mIF7cBycZCH4KMiRGqJJwZDZD"

            headers = {
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
            }
            
            payload = {
                "messaging_product": "whatsapp",
                "to": f"57{numero}",
                "type": "template",
                "template": {
                    "name": "hello", # Nombre de tu plantilla de WhatsApp
                    "language": {
                        "code": "es_CO"
                    }
                }
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()
                messages.success(request, '¡Mensaje enviado correctamente a WhatsApp!')
                return redirect('whatsapp:enviar_mensaje')

            except requests.exceptions.HTTPError as e:
                try:
                    error_data = e.response.json()
                    error_message = error_data.get('error', {}).get('message', 'Error desconocido de la API.')
                    messages.error(request, f'Error al enviar mensaje: {error_message}')
                except (ValueError, KeyError):
                    messages.error(request, f'Error de la API de WhatsApp: {e}')
            except requests.exceptions.RequestException as e:
                messages.error(request, f'Error de conexión: {e}')
    else:
        form = EnviarMensajeForm()

    return render(request, 'whatsapp/enviar_mensaje.html', {'form': form})