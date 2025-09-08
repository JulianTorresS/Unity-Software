from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

@login_required
def profile_update(request):
    if request.method == 'POST':
        # Instanciar formularios para la validación
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if 'update_profile' in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
                return redirect('profile_update')
        
        elif 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, '¡Tu contraseña ha sido actualizada con éxito!')
                return redirect('profile_update')

    else:
        # Para el método GET, inicializa los formularios vacíos
        profile_form = ProfileUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    context = {
        'profile_form': profile_form,
        'password_form': password_form
    }
    return render(request, 'profiles/profile_update.html', context)