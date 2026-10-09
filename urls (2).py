
from django.urls import path
from . import views
from .views import cerrar_sesion

urlpatterns = [
    path('', views.indice, name='indice'),
    path('acerca', views.acerca, name='acerca'),
    path('bienvenido', views.bienvenido, name='bienvenido'),
    path('contacto', views.contacto, name='contacto'),
    path('exito', views.exito, name='exito'),
    path('logout/', cerrar_sesion, name='cerrar_sesion'),
    path('sucursales', views.sucursales, name='sucursales'),
]
