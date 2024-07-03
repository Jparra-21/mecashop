from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, NegocioForm
from .models import Negocio
from .models import Suscripcion, Orden
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import os

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Negocio.objects.create(user=user)
            login(request, user)
            return redirect('infouser')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('infouser')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('index')

def infouser(request):
    if request.method == 'POST':
        form = NegocioForm(request.POST, instance=request.user.negocio)
        if form.is_valid():
            form.save()
            # Aquí puedes agregar un mensaje de éxito si lo deseas
    else:
        form = NegocioForm(instance=request.user.negocio)
    return render(request, 'infouser.html', {'form': form})

def carrito(request):
    # Lógica para el carrito de compras
    return render(request, 'carrito.html')

def index(request):
    suscripciones = Suscripcion.objects.all()
    return render(request, 'index.html', {'suscripciones': suscripciones})

@login_required
def comprar_suscripcion(request, suscripcion_id):
    suscripcion = Suscripcion.objects.get(id=suscripcion_id)
    orden = Orden.objects.create(user=request.user, suscripcion=suscripcion)
    return redirect('carrito')

@login_required
def carrito(request):
    ordenes = Orden.objects.filter(user=request.user, estado='Pendiente')
    return render(request, 'carrito.html', {'ordenes': ordenes})

@login_required
def eliminar_suscripcion(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, user=request.user)
    orden.delete()
    return redirect('carrito')

def index(request):
    suscripciones = Suscripcion.objects.all()
    image_dir = os.path.join(settings.MEDIA_ROOT, 'carousel_images')
    image_urls = [os.path.join(settings.MEDIA_URL, 'carousel_images', image) for image in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, image))]
    return render(request, 'index.html', {'suscripciones': suscripciones, 'image_urls': image_urls})