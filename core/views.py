from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Servicio, Caldera, MensajeContacto
from .forms import ContactoForm

def home(request):
    servicios = Servicio.objects.all()
    calderas = Caldera.objects.all()
    return render(request, 'core/home.html', {
        'servicios': servicios,
        'calderas': calderas
    })

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'core/servicios.html', {
        'servicios': servicios
    })

def calderas(request):
    calderas = Caldera.objects.all()
    return render(request, 'core/calderas.html', {
        'calderas': calderas
    })

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    
    return render(request, 'core/contacto.html', {
        'form': form
    })

def sobre_nosotros(request):
    return render(request, 'core/sobre_nosotros.html')
