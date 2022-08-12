from django.shortcuts import render
from database.models import producto, factura_compra, factura_unidad
from django.contrib import messages


def homepage(request):
    productos=producto.objects.all()
    proRe=[]
    """
    recu=factura.objects.filter(Id_cliecte=request.user.id)
    fact=[]
    
    for i in recu:
        facturas=factura_producto.objects.filter(Id_factura=i.ID_factura)
        fact.append(facturas)

    
    for ft in fact:
        pr=producto.objects.filter(ID_producto=ft[0].Id_producto_id)
        proRe.append(pr[0])"""


    return render(request,'html/index.html',{'productos':productos,'recurrentes':proRe})