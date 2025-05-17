from django.contrib import admin
from .models import Servicio, Caldera, MensajeContacto, Testimonio, Proyecto

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')
    list_editable = ('orden',)
    search_fields = ('titulo', 'descripcion')

@admin.register(Caldera)
class CalderaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'potencia', 'tipo', 'orden')
    list_editable = ('orden',)
    list_filter = ('tipo',)
    search_fields = ('nombre', 'potencia', 'descripcion')

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('nombre', 'email', 'mensaje')
    readonly_fields = ('fecha',)

@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'empresa', 'fecha', 'orden')
    list_editable = ('orden',)
    search_fields = ('cliente', 'empresa', 'comentario')
    readonly_fields = ('fecha',)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'fecha', 'orden')
    list_editable = ('orden',)
    search_fields = ('titulo', 'cliente', 'descripcion')
