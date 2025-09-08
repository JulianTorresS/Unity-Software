from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from .models import Translation
from .forms import TranslationForm

class TranslationListView(LoginRequiredMixin, ListView):
    model = Translation
    template_name = 'translation/listar.html'
    context_object_name = 'translations'

    def get_queryset(self):
        return Translation.objects.filter(user=self.request.user).order_by('-created_at')

@login_required
def translation_tool(request):
    form = TranslationForm()
    translated_text = None

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            original_text = form.cleaned_data['original_text']
            target_language = form.cleaned_data['target_language']

            # Lógica de la API (la misma de antes)
            api_url = f"https://api.mymemory.translated.net/get?q={original_text}&langpair=es|{target_language}"
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()
                translated_text = data['responseData']['translatedText']

                # Guarda el registro en la base de datos
                Translation.objects.create(
                    user=request.user,
                    original_text=original_text,
                    translated_text=translated_text,
                    target_language=target_language
                )
            except (requests.exceptions.RequestException, KeyError) as e:
                form.add_error(None, f"Error al traducir: {e}")

    # Obtiene el historial de traducciones para mostrarlo en la misma página
    history = Translation.objects.filter(user=request.user).order_by('-created_at')[:5] # Muestra las últimas 5

    context = {
        'form': form,
        'translated_text': translated_text,
        'history': history,
    }
    return render(request, 'translation/translation_create.html', context)

class TranslationDetailView(LoginRequiredMixin, DetailView):
    model = Translation
    template_name = 'translation/translation_detail.html'
    context_object_name = 'translation'

class TranslationDeleteView(LoginRequiredMixin, DeleteView):
    model = Translation
    template_name = 'translation/translation_confirm_delete.html'
    success_url = reverse_lazy('translation:list')