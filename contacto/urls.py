from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name='contacto'), # Se verá en ://midominio.com
]
