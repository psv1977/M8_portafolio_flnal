from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Producto, Orden, OrdenItem
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required


def home(request):
    productos = Producto.objects.filter(disponible=True)

    contexto = {
        'productos': productos
    }

    return render(request, 'tienda_online/home.html', contexto)

@staff_member_required
def lista_productos_admin(request):
    productos = Producto.objects.all()

    return render(
        request,
        'tienda_online/admin_productos/lista.html',
        {'productos': productos}
    )


@staff_member_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Producto creado correctamente.'
            )
            return redirect('lista_productos_admin')
    else:
        form = ProductoForm()

    return render(
        request,
        'tienda_online/admin_productos/formulario.html',
        {
            'form': form,
            'titulo': 'Crear producto'
        }
    )


@staff_member_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(
        Producto,
        id=producto_id
    )

    if request.method == 'POST':
        form = ProductoForm(
            request.POST,
            instance=producto
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Producto actualizado correctamente.'
            )
            return redirect('lista_productos_admin')
    else:
        form = ProductoForm(instance=producto)

    return render(
        request,
        'tienda_online/admin_productos/formulario.html',
        {
            'form': form,
            'titulo': 'Editar producto'
        }
    )


@staff_member_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(
        Producto,
        id=producto_id
    )

    if request.method == 'POST':
        producto.delete()
        messages.success(
            request,
            'Producto eliminado correctamente.'
        )
        return redirect('lista_productos_admin')

    return render(
        request,
        'tienda_online/admin_productos/eliminar.html',
        {'producto': producto}
    )

@login_required
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    carrito = request.session.get('carrito', {})
    producto_id_str = str(producto.id)

    cantidad_actual = carrito.get(producto_id_str, {}).get('cantidad', 0)

    if cantidad_actual + 1 > producto.stock:
        messages.error(request, 'No hay stock suficiente para este producto.')
        return redirect('home')

    if producto_id_str in carrito:
        carrito[producto_id_str]['cantidad'] += 1
    else:
        carrito[producto_id_str] = {
            'nombre': producto.nombre,
            'precio': producto.precio,
            'cantidad': 1
        }

    request.session['carrito'] = carrito
    messages.success(request, 'Producto agregado al carrito.')

    return redirect('home')


@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', {})

    total = 0

    for item in carrito.values():
        item['subtotal'] = item['precio'] * item['cantidad']
        total += item['subtotal']

    return render(request, 'tienda_online/carrito.html', {
        'carrito': carrito,
        'total': total
    })


@login_required
def quitar_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto_id)

    if producto_id_str in carrito:
        del carrito[producto_id_str]
        messages.success(request, 'Producto eliminado del carrito.')

    request.session['carrito'] = carrito

    return redirect('ver_carrito')

@login_required
def actualizar_carrito(request):
    if request.method == 'POST':
        carrito = request.session.get('carrito', {})

        for producto_id, item in carrito.items():
            producto = get_object_or_404(Producto, id=producto_id)
            cantidad = int(request.POST.get(f'cantidad_{producto_id}', 1))

            if cantidad <= 0:
                messages.error(request, 'La cantidad debe ser mayor que cero.')
                return redirect('ver_carrito')

            if cantidad > producto.stock:
                messages.error(
                    request,
                    f'No hay stock suficiente para {producto.nombre}. Stock disponible: {producto.stock}.'
                )
                return redirect('ver_carrito')

            item['cantidad'] = cantidad

        request.session['carrito'] = carrito
        messages.success(request, 'Carrito actualizado correctamente.')

    return redirect('ver_carrito')


@login_required
def checkout(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        messages.error(request, 'Tu carrito está vacío.')
        return redirect('home')

    # Validar stock antes de crear la orden
    for producto_id, item in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)

        if item['cantidad'] > producto.stock:
            messages.error(
                request,
                f'No hay stock suficiente para {producto.nombre}. Stock disponible: {producto.stock}.'
            )
            return redirect('ver_carrito')

    total = 0

    for item in carrito.values():
        total += item['precio'] * item['cantidad']

    orden = Orden.objects.create(
        usuario=request.user,
        total=total,
        finalizada=True
    )

    for producto_id, item in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)

        OrdenItem.objects.create(
            orden=orden,
            producto=producto,
            cantidad=item['cantidad'],
            precio_unitario=item['precio']
        )

        producto.stock -= item['cantidad']
        producto.save()

    request.session['carrito'] = {}

    messages.success(request, 'Compra confirmada correctamente.')

    return render(request, 'tienda_online/checkout.html', {
        'orden': orden
    })