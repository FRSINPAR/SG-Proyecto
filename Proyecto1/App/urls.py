from django.urls import path
from App.views import inicioApp, lista_productos, sort_lista_productos, listar_categorias, create_categories

urlpatterns = [
    path('inicioAplicacion/', inicioApp),
    path('listadoProductos/',lista_productos),
    path('listadoProductosOrderBy/',sort_lista_productos),
    path('listar_categorias/', listar_categorias),
    path('create-categories/', create_categories),
    
]