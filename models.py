
import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8,decimal_places=2, default =0)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name

class Sucursal(models.Model):
    nombre = models.CharField(max_length=64)
    direccion= models.CharField(max_length=128)
    comuna = models.CharField(max_length=64)
    telefono = models.CharField(max_length=32,blank=True)
    horario= models.CharField(max_length=64,blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.comuna}"    
