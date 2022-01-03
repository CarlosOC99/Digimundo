from django.shortcuts import render
from digimundo.models import Registro
from .models import Registro


def index(request):
  if request.method == 'POST':
        datos = Registro.objects.create(
            nombre=request.POST['nombre'], apellidos=request.POST['apellidos'], 
            correo=request.POST['correo'], telefono=request.POST['telefono'],
            empresa=request.POST['empresa'],cargo=request.POST['cargo'],
            comentarios=request.POST['comentarios'])
        datos.save()
  context = {}
  return render(request, 'social/index.html')



def servicios(request):
  return render(request, 'social/Servicios.html')

def nosotros(request):
  return render(request, 'social/Nosotros.html')

def contactanos(request):
  return render(request, 'social/Contactanos.html')


# Create your views here.
