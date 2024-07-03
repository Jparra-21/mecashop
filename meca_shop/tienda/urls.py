from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comprar/<int:suscripcion_id>/', views.comprar_suscripcion, name='comprar_suscripcion'),
    path('carrito/', views.carrito, name='carrito'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('infouser/', views.infouser, name='infouser'),
    path('eliminar/<int:orden_id>/', views.eliminar_suscripcion, name='eliminar_suscripcion'),
]