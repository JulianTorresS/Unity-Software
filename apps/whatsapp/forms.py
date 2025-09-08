from django import forms

class EnviarMensajeForm(forms.Form):
    numero = forms.CharField(label='Número de Teléfono', max_length=10, help_text='Ej: 3001234567')

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise forms.ValidationError("El número de teléfono solo debe contener dígitos.")
        return numero