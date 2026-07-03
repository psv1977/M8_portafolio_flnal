# M8_portafolio_flnal
# 🛒 TechStore - Ecommerce en Django

Proyecto final del Módulo 8 del Bootcamp Desarrollo de Aplicaciones Python-Django.

Aplicación web de comercio electrónico desarrollada con Django y PostgreSQL que permite la administración de productos, autenticación de usuarios, carrito de compras y generación de órdenes.

---

# 📌 Características

## Administrador
- Crear productos.
- Editar productos.
- Eliminar productos.
- Visualizar listado de productos.
- Gestionar el stock disponible.

## Cliente
- Registro mediante usuario del sistema.
- Inicio y cierre de sesión.
- Visualización del catálogo de productos.
- Agregar productos al carrito.
- Modificar cantidades.
- Eliminar productos del carrito.
- Confirmar compras.

## Sistema
- Validación de stock disponible.
- Generación automática de órdenes.
- Generación de detalle de productos comprados.
- Actualización automática del stock.
- Interfaz responsiva utilizando Bootstrap.

---

# 🛠 Tecnologías utilizadas

- Python 3.14
- Django 6
- PostgreSQL
- psycopg2
- Bootstrap 5
- HTML5
- CSS3
- Git
- GitHub

---

# 📁 Estructura del proyecto

```text
M8_PORTAFOLIO_FINAL/
│
├── ecommerce/
│
├── tienda_online/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── venv/
├── manage.py
├── README.md
└── .gitignore
```

---

# ⚙️ Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/psv1977/M8_PORTAFOLIO_FINAL.git
cd M8_PORTAFOLIO_FINAL
```

## 2. Crear entorno virtual

```bash
python -m venv venv
```

## 3. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux

```bash
source venv/bin/activate
```

## 4. Instalar dependencias

```bash
pip install django
pip install psycopg2
```

o bien:

```bash
pip install -r requirements.txt
```

---

# 🗄 Configuración de la Base de Datos

Crear una base de datos PostgreSQL:

```text
Nombre: ecommerce_db
Usuario: postgres
Password: ********* 
Puerto: 5432
```

Configurar en:

```python
settings.py
```

---

# 🔄 Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 👤 Crear superusuario

```bash
python manage.py createsuperuser
```

---

# ▶️ Ejecutar servidor

```bash
python manage.py runserver
```

Aplicación:

```text
http://127.0.0.1:8000/
```

Panel administrativo:

```text
http://127.0.0.1:8000/admin/
```

---

# 👥 Usuarios de prueba

## Administrador

```text
Usuario: admin
Password: admin1234
```

## Cliente

```text
Usuario: cliente
Password: Django2026$
```

---

# 🧩 Funcionalidades implementadas

- CRUD de productos.
- Autenticación de usuarios.
- Carrito de compras.
- Gestión de stock.
- Validación de disponibilidad.
- Generación de órdenes.
- Actualización automática de inventario.

---

# 📷 Capturas de pantalla

- Catálogo de productos.
- Carrito de compras.
- Administración de productos.
- Confirmación de compra.

---

# 🚀 Mejoras futuras

El proyecto puede evolucionar hacia un sistema de gestión de inventario y mantenimiento incorporando:

- Stock mínimo.
- Stock crítico.
- Punto de reorden.
- Generación automática de solicitudes de reposición.
- Integración con órdenes de trabajo.
- Movimientos de inventario.
- Trazabilidad de materiales.
- Dashboard de indicadores.
- Reportes y exportación de datos.

---

# 📚 Aprendizajes obtenidos

Durante el desarrollo de este proyecto se aplicaron conocimientos relacionados con:

- Arquitectura MVT de Django.
- ORM de Django.
- PostgreSQL.
- Gestión de usuarios y permisos.
- Formularios y validaciones.
- Manejo de sesiones.
- Diseño responsivo con Bootstrap.
- Uso de Git y GitHub para el control de versiones.

---

# 👨‍💻 Autor

**Patricio Saavedra**

Ingeniero Mecánico – MBA  
Bootcamp Desarrollo de Aplicaciones Python-Django  
GitHub: https://github.com/psv1977