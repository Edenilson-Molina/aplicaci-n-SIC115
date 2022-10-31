"""contastation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contaapp import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('logout', views.login),
    path('index',views.index),
    path('costoMO',views.costoMO),
    path('costoP',views.costoP),
    path('balanceCompro',views.balanceCompro),
    path('estadoResultado',views.estadoResultado),
    path('estadoCapital',views.estadoCapital),
    path('balanceGeneral',views.balanceGeneral),
    path('ventas',views.ventas),
    path('compras',views.compras),
    path('gastos',views.gastos),
    path('ingresarOrden/',views.ingresarOrden),
    path('ingresarVenta/',views.ingresarVenta),
    path('ingresarCompra/',views.ingresarCompra),
    path('ingresarGasto/',views.ingresarGasto),
    
]


urlpatterns += staticfiles_urlpatterns()