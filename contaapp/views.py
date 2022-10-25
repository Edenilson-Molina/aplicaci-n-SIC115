from django.shortcuts import render

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