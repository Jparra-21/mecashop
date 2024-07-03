from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Negocio

@receiver(post_save, sender=User)
def create_negocio_profile(sender, instance, created, **kwargs):
    if created:
        Negocio.objects.create(nombre=instance)

@receiver(post_save, sender=User)
def save_negocio_profile(sender, instance, **kwargs):
    if hasattr(instance, 'negocio'):
        instance.negocio.save()
    else:
        Negocio.objects.create(nombre=instance)