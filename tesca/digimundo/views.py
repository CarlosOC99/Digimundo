from django.shortcuts import render
from digimundo.models import Registro
from .models import Registro
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def index(request):
  if request.method == 'POST':
        correoD=request.POST['correo']

        datos = Registro.objects.create(
            nombre=request.POST['nombre'], apellidos=request.POST['apellidos'], 
            correo=request.POST['correo'], telefono=request.POST['telefono'],
            empresa=request.POST['empresa'],cargo=request.POST['cargo'],
            comentarios=request.POST['comentarios']
            )
        datos.save()

        send_mail(
    'Correo de Confirmacion',
    'Hola, Recibimos tu correo y en breve nos comunicaremos contigo para mas informacion 🐍',
    settings.EMAIL_HOST_USER,
    [correoD,'tescacorpora@gmail.com'],
    fail_silently=False
)

  context = {}

  return render(request, 'social/index.html')

def servicios(request):
  return render(request, 'social/Servicios.html')

def nosotros(request):
  return render(request, 'social/Nosotros.html')

def contactanos(request):
  return render(request, 'social/Contactanos.html')


# Create your views here.