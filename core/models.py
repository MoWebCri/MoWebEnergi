from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios/')
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.titulo

class Caldera(models.Model):
    nombre = models.CharField(max_length=100)
    potencia = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='calderas/')
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Caldera'
        verbose_name_plural = 'Calderas'

    def __str__(self):
        return f"{self.nombre} - {self.potencia}"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contacto'

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
