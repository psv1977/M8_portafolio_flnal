from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'administracion/productos/',
        views.lista_productos_admin,
        name='lista_productos_admin'
    ),
    path(
        'administracion/productos/crear/',
        views.crear_producto,
        name='crear_producto'
    ),
    path(
        'administracion/productos/editar/<int:producto_id>/',
        views.editar_producto,
        name='editar_producto'
    ),
    path(
        'administracion/productos/eliminar/<int:producto_id>/',
        views.eliminar_producto,
        name='eliminar_producto'
    ),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/quitar/<int:producto_id>/', views.quitar_carrito, name='quitar_carrito'),
    path('carrito/actualizar/', views.actualizar_carrito, name='actualizar_carrito'),
    path('checkout/', views.checkout, name='checkout'),
]