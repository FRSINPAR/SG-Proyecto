from django.shortcuts import render
from Orders.models import Order

def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    } 
    return render(request,'orders/list_orders.html',context)