# apps/translation/forms.py - NO CHANGES NEEDED
from django import forms
from .models import Translation

LANGUAGES = [
    ('en', 'Inglés'),
    ('fr', 'Francés'),
    ('de', 'Alemán'),
    ('it', 'Italiano'),
    ('pt', 'Portugués'),
    ('zh', 'Chino (Mandarín)'),
    ('ru', 'Ruso'),
    ('ja', 'Japonés'),
    ('ko', 'Coreano'),
    ('ar', 'Árabe'),
    ('hi', 'Hindi'),
]

class TranslationForm(forms.Form):
    original_text = forms.CharField(
        label="Texto a traducir",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    target_language = forms.ChoiceField(
        label="Idioma de destino",
        choices=LANGUAGES,
        widget=forms.RadioSelect
    )