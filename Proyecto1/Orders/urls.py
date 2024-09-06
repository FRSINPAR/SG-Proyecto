from django.urls import path
from App.views import inicioApp, lista_productos, sort_lista_productos, listar_categorias, create_categories
from Orders.views import order_list

urlpatterns = [

    path('list-orders/', order_list ),
]