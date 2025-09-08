from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Importa el formulario desde el nuevo archivo forms.py
from .forms import CustomUserCreationForm 

@login_required
def home(request):
    """
    Vista de la página principal (landing page)
    Solo accesible para usuarios autenticados.
    """
    return render(request, 'core/home.html')

def register(request):
    """
    Vista para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '¡Tu cuenta ha sido creada con éxito! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Credenciales inválidas. Por favor, intenta de nuevo.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')