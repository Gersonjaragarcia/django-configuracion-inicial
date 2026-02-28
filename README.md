# Django Cap01: Fundamentos
En este capitulo inicio mi prtafolio de este importante framework de python

## Conceptos dominados:
- Instalación de Django 5.1.
- Estructura de archivos de un proyecto (`core/` y `manage.py`).
- Uso del servidor de desarrollo.

## Cómo correrlo:
1. Clonar el repo.
2. `pip install -r requirements.txt`
3. `python manage.py runserver`

## Proyecto vs. Aplicación (Apps)
Una de las primeras lecciones clave es diferenciar estos dos comandos esenciales:

*   **`django-admin startproject core .`**: Crea el "corazón" del sitio (ajustes globales, base de datos, seguridad).
*   **`python manage.py startapp main`**: Crea un módulo funcional específico. Un proyecto puede tener múltiples apps (ej: usuarios, blog, tienda). 
---

## Flujo de Trabajo para crear una funcionalidad

Para que una página sea visible en Django, seguí este flujo de 4 pasos:

### 1. Creación de la App
Generación de la estructura de carpetas necesaria para la lógica del negocio.
```bash
python manage.py startapp main.

## 2. Registro de la Aplicación

Django es un sistema modular. Para que el proyecto reconozca las funciones, modelos y configuraciones de nuestra nueva app, debemos darla de alta en el archivo de configuración global.

*   **Archivo:** `core/settings.py`
*   **Acción:** Añadir `'main',` a la lista de `INSTALLED_APPS`.

```python
# core/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Mis Aplicaciones (Apps locales)
    'main', 
]

### 3. Creación de la Vista (La Lógica)
La vista es la función que procesa la petición del usuario y devuelve una respuesta.

*   **Archivo:** `main/views.py`
*   **Código:**

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>¡Bienvenido a mi primera App en Django!</h1>")

## Estructura del Proyecto

Para mantener el código organizado y escalable, el proyecto sigue una arquitectura modular dividida en aplicaciones independientes:

```text
cap01_Basico/
├── core/              # Configuración global del proyecto (settings, urls principales)
├── main/              # Aplicación principal (Landing page)
│   ├── urls.py        # Rutas específicas de la app
│   └── views.py       # Lógica de la página de inicio
├── blog/              # Aplicación de Blog
│   ├── urls.py        # Rutas del blog (/blog/)
│   └── views.py       # Lógica de artículos y listados
├── contacto/          # Aplicación de Contacto
│   ├── urls.py        # Rutas de contacto (/contacto/)
│   └── views.py       # Lógica de formularios de contacto
└── manage.py          # Utilidad de línea de comandos de Django
