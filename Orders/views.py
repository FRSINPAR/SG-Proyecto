from django.shortcuts import render
from django.http import HttpResponse
from Orders.models import Order
from datetime import *
import random

def newOrderList(request):
    productos = [
        "Rollo de cocina", "Rollo de papel", "Servilletas", "Toalla de cocina",
        "Papel aluminio", "Papel encerado", "Bolsas de plástico", "Papel higiénico",
        "Esponjas", "Limpiador multiusos", "Jabón para platos", "Desinfectante",
        "Paño de cocina", "Guantes de cocina", "Cepillo de limpieza"
    ]
    clientes = [
    'Papelería Nacional S.A.',
    'Papel y Cartón Ltd.',
    'Industria del Papel S.A.',
    'Grupo Papelero del Norte',
    'Papel y Envases Globales',
    'Papelería El Águila',
    'Papel y Más S.R.L.'
    ]

    for i in range(len(productos)):
        client = random.choice(clientes)
        payment_method =  random.choice([choice[0] for choice in Order.CHOICES])
        product = random.choice(productos)

        Order.objects.create(product=product, payment_method=payment_method, client=client)
    creacionOrdenes=f"SE CREO NUEVA TABLA DE ORDENES - cantidad creada: {len(productos)} - fecha: {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')} -" 
    return HttpResponse(creacionOrdenes)

def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    } 
    return render(request,'orders/list_orders.html',context=context)