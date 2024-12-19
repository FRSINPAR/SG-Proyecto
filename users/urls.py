from django.urls import path
from . import views  # Asegúrate de que las vistas existen

from .views import loginView, signUp, logoutView
from Proyecto1.views import index
from django.contrib.auth.views import LogoutView

#path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout') -> Este metodo viene con DJANGO, pero no podia validar un 'cancelar' al momento de hacer un logout de sesión.
urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('signup/', signUp, name='signup'),
    path('', index, name='home'),
]