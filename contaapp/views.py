from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")

def costoMO(request):
    return render(request, "costoMO.html")
    
def costoP(request):
    return render(request, "costoP.html")

def balanceCompro(request):
    return render(request, "balanceCompro.html")

def estadoResultado(request):
    return render(request, "estadoResultado.html")

def estadoCapital(request):
    return render(request, "estadoCapital.html")

def balanceGeneral(request):
    return render(request, "balanceGeneral.html")

def compras(request):
    return render(request, "compras.html")

def ventas(request):
    return render(request, "ventas.html")

def gastos(request):
    return render(request, "gastos.html")

#Para guardar los Elementos del costo en base de datos
def ingresarOrden(request):
    try:
        cantidadP = float(request.POST['txtCantidad'])
        materiaDirecta = float(request.POST['txtUno'])
        manoObraDirecta = float(request.POST['txtDos'])
        costoIndirecto = float(request.POST['txtTres'])

        materiaDirecta = materiaDirecta*cantidadP
        manoObraDirecta = manoObraDirecta*cantidadP
        costoIndirecto = costoIndirecto*cantidadP


        objetoMD = Cuenta.objects.get(idcuenta = 4102)
        objetoMD.debecuenta += materiaDirecta
        objetoMD.save()

        objetoMOD = Cuenta.objects.get(idcuenta =4101)
        objetoMOD.debecuenta +=manoObraDirecta
        objetoMOD.save()

        objetoCIF = Cuenta.objects.get(idcuenta = 4103)
        objetoCIF.debecuenta += costoIndirecto
        objetoCIF.save()
        messages.success(request,'¡Orden de fabricación registrada con éxito!')
    except Exception as e:
        messages.error(request,'No fue posible registrar orden de fabricación')

    return redirect('/costoP')