from django.contrib import admin
from .models import Servicio, Caldera, MensajeContacto

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
