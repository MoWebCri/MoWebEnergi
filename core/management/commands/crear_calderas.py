from django.core.management.base import BaseCommand
from core.models import Caldera

class Command(BaseCommand):
    help = 'Crea las calderas iniciales del catálogo'

    def handle(self, *args, **kwargs):
        calderas_data = [
            {
                'nombre': 'Cleaver Brooks',
                'potencia': '12.000 KHV',
                'tipo': 'Alta Capacidad',
                'descripcion': 'Caldera de alta eficiencia para grandes instalaciones industriales. Sistema dual fuel para máxima flexibilidad operativa.',
                'orden': 1
            },
            {
                'nombre': 'Paradies',
                'potencia': '10.000 KHV',
                'tipo': 'Media-Alta Capacidad',
                'descripcion': 'Caldera industrial de alta eficiencia, ideal para procesos que requieren gran capacidad de generación de vapor.',
                'orden': 2
            },
            {
                'nombre': 'ABCO',
                'potencia': '8.000 KHV',
                'tipo': 'Media Capacidad',
                'descripcion': 'Caldera industrial versátil, perfecta para instalaciones de tamaño medio que requieren eficiencia y confiabilidad.',
                'orden': 3
            },
            {
                'nombre': 'Geat Transfer',
                'potencia': '5.300 KHV',
                'tipo': 'Media Capacidad',
                'descripcion': 'Caldera industrial de media capacidad, ideal para procesos que requieren generación de vapor moderada.',
                'orden': 4
            },
            {
                'nombre': 'ICI',
                'potencia': '5.100 KHV',
                'tipo': 'Media Capacidad',
                'descripcion': 'Caldera industrial de media capacidad, diseñada para procesos que requieren eficiencia y confiabilidad.',
                'orden': 5
            },
            {
                'nombre': 'Vapor Industrial',
                'potencia': '4.000 KHV',
                'tipo': 'Media Capacidad',
                'descripcion': 'Caldera industrial versátil para procesos que requieren generación de vapor moderada.',
                'orden': 6
            },
            {
                'nombre': 'ICI',
                'potencia': '4.270 KHV',
                'tipo': 'Baja Capacidad',
                'descripcion': 'Caldera industrial de baja capacidad, perfecta para instalaciones pequeñas que requieren eficiencia.',
                'orden': 7
            },
            {
                'nombre': 'Socometal',
                'potencia': '1.500 KHV',
                'tipo': 'Baja Capacidad',
                'descripcion': 'Caldera industrial compacta, ideal para instalaciones pequeñas que requieren generación de vapor.',
                'orden': 8
            },
            {
                'nombre': 'Bríones',
                'potencia': '1.000 KHV',
                'tipo': 'Baja Capacidad',
                'descripcion': 'Caldera industrial compacta que funciona con diesel, perfecta para instalaciones pequeñas.',
                'orden': 9
            }
        ]

        for caldera_data in calderas_data:
            Caldera.objects.get_or_create(
                nombre=caldera_data['nombre'],
                potencia=caldera_data['potencia'],
                defaults=caldera_data
            )
            self.stdout.write(
                self.style.SUCCESS(f'Caldera "{caldera_data["nombre"]}" creada exitosamente')
            ) 