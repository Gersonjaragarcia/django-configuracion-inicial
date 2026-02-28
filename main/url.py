from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Aquí defines que esta es la raíz real
]
