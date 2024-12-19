from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import time
# def loginView(request):
#     if request.method == 'GET':
#         formulario = AuthenticationForm()
#         context = {
#             'formulario':formulario
#         }
#         return render(request,  'users/login.html', context=context)

def loginView(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST, request=request)
        if formulario.is_valid():
            # Obtener las credenciales del formulario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Iniciar sesión
                login(request, user)
                return redirect('/')  # Cambia 'home' a la vista que prefieras
            else:
                # Si las credenciales no son correctas, mostrar un mensaje de error
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            if formulario.non_field_errors():
                # Manejar errores no asociados a campos específicos (credenciales incorrectas)
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
            else:
                # Manejar otros errores (como campos vacíos)
                messages.error(request, "Por favor, corrige los errores en el formulario.")
                print(formulario.errors)
    
    else:
        formulario = AuthenticationForm()

    context = {
        'formulario': formulario
    }
    return render(request, 'users/login.html', context)

def logoutView(request):
    if request.method == 'POST':
        # Cerrar sesión y redirigir al login
        logout(request)
        messages.success(request, "Has cerrado sesión exitosamente.")
        return redirect('login')  # Nombre de la ruta para iniciar sesión
    else:
        # Renderizar la página de confirmación para cerrar sesión
        return render(request, 'users/logout.html')
    
def signUp(request):
    return render(request, 'inicio/index.html', context={})


