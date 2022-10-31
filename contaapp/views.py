from asyncio.windows_events import NULL
import datetime
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

def devuelveMes():
    mes = datetime.date.today().month
    if(mes == 1): mes = 'Enero'
    if(mes == 2): mes = 'Febrero'
    if(mes == 3): mes = 'Marzo'
    if(mes == 4): mes = 'Abril'
    if(mes == 5): mes = 'Mayo'
    if(mes == 6): mes = 'Junio'
    if(mes == 7): mes = 'Julio'
    if(mes == 8): mes = 'Agosto'
    if(mes == 9): mes = 'Septiembre'
    if(mes == 10): mes = 'Octubre'
    if(mes == 11): mes = 'Noviembre'
    if(mes == 12): mes = 'Diciembre'
    return mes

def balanceCompro(request):
    return render(request, "balanceCompro.html")

def estadoResultado(request):
    mes = devuelveMes()
    ventaTotal = Cuenta.objects.get(idcuenta = 5101)
    deudora = []
    gastos = []
    ventasNetas = ventaTotal.habercuenta
    costoVentas = 0.0
    utilidadBruta = 0.0
    totalGastos = 0.0
    utilidadAntesImpuesto = 0.0
    for i in Cuenta.objects.filter(idrubro = 41):
        deudora.append({'idcuenta':i.idcuenta,'nomcuenta': i.nomcuenta,'debecuenta': i.debecuenta})
        if (i.idcuenta == 4106 or i.idcuenta == 4107):
            if(i.debecuenta > 0):
                ventasNetas -= i.debecuenta
        if(i.idcuenta == 4101 or i.idcuenta ==4102 or i.idcuenta ==4103):
            costoVentas += i.debecuenta
    for i in Cuenta.objects.filter(idrubro = 42):
        gastos.append({'idcuenta':i.idcuenta,'nomcuenta': i.nomcuenta,'debecuenta': i.debecuenta})
        totalGastos += i.debecuenta
    utilidadBruta = ventasNetas - costoVentas
    utilidadAntesImpuesto = utilidadBruta - totalGastos
    return render(request, "estadoResultado.html",{"mes":mes,"ventaTotal":ventaTotal,"deudora":deudora,
    "ventasNetas":ventasNetas,"costoVentas":costoVentas,"utilidadBruta":utilidadBruta,
    "gastos":gastos,"totalGastos":totalGastos,"utilidadAntesImpuesto":utilidadAntesImpuesto})


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

def ingresarVenta(request):    

    try:
        montoVenta = float(request.POST['txtuno'])
    
        IVADebito = float(request.POST['txtdos'])

        tipoVenta = request.POST['txttres']
        
        # //CAMBIOS inicio
        objetoCuentaCobrar = Cuenta.objects.get(idcuenta= 1102)
        objetoCaja = Subcuenta.objects.get(idsubcuenta=110101)
        if (tipoVenta == "contado"):      
            objetoCaja.debe_subcuenta += montoVenta
            objetoCaja.save()
        if (tipoVenta == "credito"):      
            objetoCuentaCobrar.debecuenta += montoVenta
            objetoCuentaCobrar.save()
        
        objetoVentas = Cuenta.objects.get(idcuenta= 5101)
        objetoVentas.habercuenta += montoVenta
        objetoVentas.save()
        objetoIVADebito = Cuenta.objects.get(idcuenta=2104)
        objetoIVADebito.habercuenta += IVADebito
        objetoIVADebito.save()

        # //CAMBIOS fin
        messages.success(request,'¡venta registrada!')
    except Exception as e:
        messages.error(request,'No fue posible registrar venta')
    return redirect('/ventas')

def ingresarCompra(request):    

    try:
        montoCompra = float(request.POST['txtuno'])
    
        IVACredito = float(request.POST['txtdos'])

        tipoVenta = request.POST['txttres']
        
        # //CAMBIOS inicio
        objetoCuentaPagar = Cuenta.objects.get(idcuenta= 2101)
        objetoCaja = Subcuenta.objects.get(idsubcuenta=110101)
        if (tipoVenta == "contado"):      
            objetoCaja.haber_subcuenta+= montoCompra
            objetoCaja.save()
        if (tipoVenta == "credito"):      
            objetoCuentaPagar.habercuenta += montoCompra
            objetoCuentaPagar.save()
        
        objetoCompras = Cuenta.objects.get(idcuenta=4104)
        objetoCompras.debecuenta += montoCompra
        objetoCompras.save()
        objetoIVACredito = Cuenta.objects.get(idcuenta=1107)
        objetoIVACredito.habercuenta += IVACredito
        objetoIVACredito.save()
        # //CAMBIOS fin
        messages.success(request,'¡compra registrada!')
    except Exception as e:
        messages.error(request,'No fue posible registrar compra')
    return redirect('/compras')



def ingresarGasto(request): 
    try:
        montoGasto = float(request.POST['txtuno'])
    
        tipoGasto = request.POST['txtdos']

        tipoPagoGasto = request.POST['txttres']

        objetoGastoAdministra = Cuenta.objects.get(idcuenta=4201)
        objetoGastoVenta = Cuenta.objects.get(idcuenta=4202)
        objetoGastoDepre = Cuenta.objects.get(idcuenta=4203)
        objetoGastoAlquiler = Cuenta.objects.get(idcuenta=4204)
        
        if (tipoGasto == "administracion"):
            objetoGastoAdministra.debecuenta += montoGasto
            objetoGastoAdministra.save()

        if (tipoGasto == "ventas"): 
            objetoGastoVenta.debecuenta += montoGasto
            objetoGastoVenta.save()
        
        if(tipoGasto == "depreciacion"):
            objetoGastoDepre.debecuenta += montoGasto
            objetoGastoDepre.save()

        if(tipoGasto == "alquiler"):
            objetoGastoAlquiler.debecuenta += montoGasto
            objetoGastoAlquiler.save()

        objetoCaja = Subcuenta.objects.get(idsubcuenta=110101)
        objetoRetencion = Cuenta.objects.get(idcuenta =2107)
        objetoDepreciacion = Cuenta.objects.get(idcuenta =1202)

        
        if (tipoPagoGasto == "caja"):
            objetoCaja.haber_subcuenta+= montoGasto
            objetoCaja.save()

        if (tipoPagoGasto == "retencion"):
            objetoRetencion.habercuenta += montoGasto
            objetoRetencion.save()

        if (tipoPagoGasto == "depreciacion"):
            objetoDepreciacion.habercuenta += montoGasto
            objetoDepreciacion.save()           

        messages.success(request,'¡Gasto registrado!')
    except Exception as e:
        messages.error(request,'No fue posible registrar compra')
    return redirect('/gastos')