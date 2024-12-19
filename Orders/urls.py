from django.urls import path
from Orders.views import order_list, newOrderList

urlpatterns = [

    path('list-orders/', order_list ),
    path('create-orders/', newOrderList ),
]