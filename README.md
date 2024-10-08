# CRUD Inventario con Flask

## Descripción

Este proyecto es una aplicación web CRUD para la gestión de inventarios, desarrollado con **Flask** y **MySQL**. Los usuarios pueden registrar, editar, eliminar y visualizar productos de su inventario personal. Además, la aplicación incluye un sistema de autenticación con registro de usuarios y protección de rutas.

## Tabla de Contenidos

1. [Características](#características)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Instalación](#instalación)
4. [Uso](#uso)
5. [Rutas Principales](#rutas-principales)
6. [Contribución](#contribución)
7. [Licencia](#licencia)

## Características

- Registro e inicio de sesión de usuarios.
- Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para productos del inventario.
- Autenticación con **Flask-Login**.
- Protección de rutas, solo accesibles a usuarios autenticados.
- Validación de permisos de usuario para editar/eliminar productos.
- Plantillas HTML personalizadas usando **Jinja2**.
- Conexión a base de datos MySQL para almacenamiento de datos.

## Tecnologías Utilizadas

- **Flask**: Framework web de Python.
- **Flask-SQLAlchemy**: ORM para manejar la base de datos.
- **Flask-Login**: Gestión de sesiones de usuarios.
- **MySQL**: Base de datos relacional.
- **Jinja2**: Motor de plantillas para HTML.

## Instalación

### Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.x**
- **MySQL**
- **Git**

### Clonar el Repositorio

```bash
git clone https://github.com/MateoRosero/Crud-inventario.git
cd Crud-inventario/Inventario/src

## Navega al directorio del proyecto

- cd Crud-inventario/Inventario/src

## Instalar las dependencias

- pip install -r requirements.txt

## Configurar las credenciales de la base de datos

- app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://TU_USUARIO:TU_CONTRASEÑA@localhost/dbInventario'

## Iniciar la aplicación

- python app.py

## Uso de la aplicación

## Registro de usuarios

- Dirígete a la página de registro en http://127. 0.0.1:5000/register.
- Crea un nuevo usuario con un nombre de usuario y contraseña.

## Iniciar sesión

- Inicia sesión en la página http://127.0.0.1:5000/login.
- Una vez autenticado, serás redirigido a la página principal del inventario.

## Gestión de productos

- Crear un nuevo producto : En la página principal del inventario, rellene el formulario de creación con el nombre del producto, la descripción y la fecha de vencimiento.
- Editar producto : Haz clic en el enlace "Editar" junto al producto que deseas modificar.
- Eliminar producto : Haga clic en "Eliminar" y confirme la eliminación del producto.

## Estructura del proyecto

Inventario/
│
├── src/
│   ├── __pycache__/
│   ├── templates/
│   │   ├── editar_producto.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   ├── app.py
│   └── database.py
└── instance/
    └── inventario.db

- app.py: Contiene la lógica principal de la aplicación, rutas y manejo de usuarios y productos.
- database.py: Archivo de conexión a la base de datos MySQL.
- templates/: Carpeta que contiene las plantillas HTML para el frontend.
