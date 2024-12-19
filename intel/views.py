from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
from intel.models import Products #IMPORTO EL MODELO DE LA APLICACION (APP)
from intel.models import Category #IMPORTO EL MODELO DE LA APLICACION (APP)
from intel.models import Documentos
from intel.forms import ProductForms #IMPORTO EL FORMULARIO LINKEADO AL MODELO DE PRODUCTS.
import random
# Create your views here.

#_________________________________

def inicioApp(request): # Datos para crear productos!
    
    nombres = [ 
        "Rollo de cocina", "Rollo de papel", "Servilletas", "Toalla de cocina",
        "Papel aluminio", "Papel encerado", "Bolsas de plástico", "Papel higiénico",
        "Esponjas", "Limpiador multiusos", "Jabón para platos", "Desinfectante",
        "Paño de cocina", "Guantes de cocina", "Cepillo de limpieza"
    ]

    # Crear 15 instancias de Producto
    for i in range(len(nombres)):
        name = random.choice(nombres)
        price = round(random.uniform(100, 1000), 2)  # Precio aleatorio entre 100 y 1000
        stock = random.choice([True, False])
        Products.objects.create(name=name, price=price, stock=stock)
    
    creacionProducto=f"SE CREO NUEVA TABLA DE PRODUCTOS - cantidad creada: {len(nombres)} - fecha: {fechaActualApp()} -"
    
    return HttpResponse(creacionProducto)
#_________________________________
def createProduct(request):


    context ={'fechaActual':fechaActualApp(),
              'form': ProductForms(),
              
              }
    if request.method == 'GET':
        return render(request, "app/nuevo_producto.html", context) #pasa los campos
    else: # Método 'POST'
        Products.objects.create(name=request.POST['nombre'], price=request.POST['precio'])
        #print (request.POST)
        
        return render(request, "app/nuevo_producto.html", context)
    
    #Products.objects.create(name=name, price=price, stock=stock)
    
     
#__________________________________ 

def fechaActualApp():

    hoy = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    return hoy

#_________________________________

def lista_productos(request):
    
    all_products = Products.objects.all()
    cantidad = len(all_products)
    for producto in all_products:
        print(producto.name)
    context = {'productos':all_products,
               'cantidad':cantidad
               }
    return render(request, "lista_productos.html", context)
#__________________________________

def sort_lista_productos(request):
    all_products = Products.objects.all().order_by('name')
    cantidadDeProductos = len(all_products)
    context={
        'productos':all_products,
        'cantidad':cantidadDeProductos
            }
    return render(request, 'lista_productos.html', context )
#__________________________________
def listar_categorias(request):

    all_cateogrias = Category.objects.all().order_by('name')
    cantidad=len(all_cateogrias)
    context = {
        'categorias':all_cateogrias,
        'cantidad':cantidad
        }
    return render(request, 'listaCategorias.html', context )

#__________________________________
def create_categories(request):
    # Datos para crear productos
    categorias = [
    "Industria Alimentaria", "Industria Farmacéutica", "Industria de Limpieza",
    "Industria Química", "Industria Textil", "Industria del Plástico",
    "Industria de Equipos de Protección Personal", "Industria del Papel y Cartón",
    "Industria de Materiales de Construcción", "Industria de Energía y Recursos Naturales",
    "Industria Electrónica", "Industria Automotriz", "Industria de Productos de Consumo",
    "Industria del Mueble y Decoración", "Industria del Calzado y Moda"
    ]
    
    # Crear 15 instancias de Categorias
    for i in range(len(categorias)):
        name = categorias[i]
        
        Category.objects.create(name=name)
    
    creacionDeCategorias=f"SE CREO NUEVA TABLA DE PRODUCTOS - cantidad creada: {len(categorias)} - fecha: {fechaActualApp()} -"
    
    return HttpResponse(creacionDeCategorias)
#___________________________________
def documentos_filtrados(request, tipo):
    
    RUBROS_MAP = {
    'manual-y-politica' : 1,
    'certificados' : 2,
    'procedimientos-generales' : 3,
    'practicas-operativas' : 4,
    'registros' : 5,
    'planes' : 6,
    'normas' : 7,
    'hojas-de-seguridad' : 8,
    'descripcion-de-procesos' : 9,
    'analisis-de-aspectos-e-impactos-ambientales' : 10,
    'pasos-individuales' : 11,
    'identificacion-de-peligro' : 12,
    'trabajo-seguro' : 13,
    'especificaciones-tecnicas' : 14,
    'materiales' : 15,
    'inventario-marketing' : 16,
    'plantillas' : 17,
    'etcs' : 19,
    }
    rubro_id = RUBROS_MAP.get(tipo)
    documentos = Documentos.objects.filter(pungrupo=rubro_id)
    return render(request, 'inicio/index.html', {'documentos': documentos, 'tipo': tipo})