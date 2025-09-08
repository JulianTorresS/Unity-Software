# apps/profiles/forms.py

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', max_length=150, required=True)
    last_name = forms.CharField(label='Apellido', max_length=150, required=True)
    email = forms.EmailField(label='Correo Electrónico', required=True) # <--- HACER OBLIGATORIO
    photo = forms.ImageField(label='Foto de Perfil', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    # ... el resto de tu código de __init__ y save ...
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'photo':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control rounded-pill bg-light border-0',
                    'placeholder': ''
                })
        if self.instance:
            self.initial['first_name'] = self.instance.first_name
            self.initial['last_name'] = self.instance.last_name
            self.initial['email'] = self.instance.email

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        
        if 'photo' in self.cleaned_data and self.cleaned_data['photo']:
            profile = user.profile
            profile.photo = self.cleaned_data['photo']
            profile.save()
        
        return user

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control rounded-pill bg-light border-0',
                'placeholder': ''
            })