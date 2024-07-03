from django.db import models
from django.contrib.auth.models import User

class Negocio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    newsletter = models.BooleanField(default=False)
    creation_date = models.DateField(blank=True, null=True)
    num_employees = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.email if self.user else "No user"
    
class Suscripcion(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Orden {self.id} de {self.user.email}"