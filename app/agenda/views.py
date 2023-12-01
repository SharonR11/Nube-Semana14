from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpRequest
from .models import Persona
from django.db.models import Q

@login_required
def menu(request):
    persona_list=Persona.objects.all()
    context={"persona_list":persona_list}
    return render(request,'plantilla/menu.html',context)

#Crear Persona
def insertarpersona(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtnombre')
        apellido = request.POST.get('txtapellido')
        email = request.POST.get('txtemail')
        celular = request.POST.get('txtcelular')
        fecha_nac=request.POST.get("txtfecha_nac") 
        foto = request.FILES.get("txtfoto")

        persona = Persona(
            nombre=nombre,
            apellido=apellido,
            email=email,
            celular=celular,
            fecha_nac=fecha_nac
        )

        if foto:
            persona.foto = foto

        # Guarda la instancia de Persona en la base de datos
        persona.save()
    return redirect('/')

def datapersona(request,idPersona):
    persona=Persona.objects.get(idPersona=idPersona)
    context={"persona":persona}
    return render(request, 'plantilla/editar.html', context)

#Editar Contacto
def editar(request,idPersona):
    persona=get_object_or_404(Persona,idPersona=idPersona)

    if request.method == 'POST':
        nombre = request.POST.get('txtnombre')
        apellido = request.POST.get('txtapellido')
        email = request.POST.get('txtemail')
        celular = request.POST.get('txtcelular')
        fecha_nac=request.POST.get("txtfecha_nac") 
        foto = request.FILES.get("txtfoto")

        persona.nombre = nombre
        persona.apellido = apellido
        persona.email = email
        persona.celular = celular
        persona.fecha_nac=fecha_nac
        persona.foto=foto

        # Guardar los cambios en la venta
        persona.save()

        # Redireccionar a una página de éxito o a la página de detalles de la venta
        return redirect('/')
    return render(request, '/', {'persona': persona})

#Eliminar Contacto
def eliminar(request, idPersona):

    persona = Persona.objects.get(idPersona=idPersona)
    persona.delete()
    return redirect('/')

def is_ajax(request: HttpRequest) -> bool:
    return request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def buscar(request):
    apellido = request.GET.get('apellido', '')
    persona_list = Persona.objects.filter(apellido__icontains=apellido)
    return render(request, 'plantilla/menu.html', {'persona_list': persona_list})


def perfil(request,idPersona):
    persona=Persona.objects.get(idPersona=idPersona)
    context={"persona":persona}
    return render(request, 'plantilla/perfil.html', context)