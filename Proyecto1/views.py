from django.http import HttpResponse
from datetime import datetime


from django.shortcuts import render

def pruebaView(request):
    
    return HttpResponse("prueba de vista")
#-------------------------------
def documents(request):
    
    context = {
        "fechaActual" : fechaActual(),
        }
    return render(request, 'documents.html', context)
#-------------------------------
def fechaActual():

    hoy = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    return hoy
#-------------------------------
def consulta(request, edad):

    return HttpResponse(f"la edad es: {edad}")
#-------------------------------
def viewTemplate(request):

#    context = {
#        "titulo" : "Página de inicio",
#        "mensaje":"Ésta es la descripcion o el resumen de la página de inicio",
#        "year":datetime.now().year
#        }

    return render(request, r'template2.html', context={})
#-------------------------------
def testeandoHtml(request):
    return render(request, 'template2.html', context={})


#-------------------------------
def pruebaTemplateContext(request):
    nombre = 'Franco'
    edad=27
    array=["lunes","martes","miercoles","jueves","viernes","Sabado"]
    context = {'nombre':nombre,
               'edad':edad,
               'array':array,
               }
    return render(request, 'contexto.html', context)
#_________________________________
def index(request):

    return render(request, 'inicio/index.html', context={}) #contra-barra exclusivo en windows

#_________________________________










