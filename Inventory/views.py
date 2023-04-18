
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Inventory.models import Producto, Transaccion
from .forms import AgregarProductoForm, CompraVentaForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = AgregarProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def eliminar_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

@require_POST
def registrar_compra_venta(request):
    form = CompraVentaForm(request.POST)
    if form.is_valid():
        producto = form.cleaned_data['producto']
        tipo = form.cleaned_data['tipo']
        fecha = form.cleaned_data['fecha']
        cantidad = form.cleaned_data['cantidad']
        precio_unitario = form.cleaned_data['precio_unitario']

        if tipo == 'C':
            producto.stock += cantidad
        else:
            producto.stock -= cantidad

        transaccion = Transaccion(producto=producto, tipo=tipo, fecha=fecha, cantidad=cantidad, precio_unitario=precio_unitario)
        transaccion.save()
        producto.save()

        return redirect('listar_productos')

    return render(request, 'registrar_compra_venta.html', {'form': form})
