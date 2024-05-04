from django.shortcuts import render, redirect
from .models import Poliza, Empleado

# Create your views here.

def index(request):
    #ordenar busqueda por asegurado
    polizas = Poliza.objects.order_by('asegurado')
   
    return render(request, 'index.html', {'polizas': polizas})

def registrarPoliza(request):
    #recupero los valores que viene del formulario de nuevaPoliza
    NroPoliza = request.POST["poliza"]
    #que asegurado quede en mayusculas
    asegurado = request.POST["asegurado"].upper()
    cuit = request.POST["CUIT"]
    fecha = request.POST["fecha"]
    poliza = Poliza.objects.create(poliza=NroPoliza, asegurado=asegurado, CUIT=cuit, fecha=fecha)

    #redirijo al home
    return redirect('/')

def nuevaPoliza(request):
    return render(request, 'nuevaPoliza.html')

def edicionPoliza(request, id):
    poliza = Poliza.objects.get(id=id)
    return render(request, 'edicionPoliza.html', {
        'poliza': poliza
    })  

def editarPoliza(request, id):
    poliza = Poliza.objects.get(id=id)
    poliza.poliza = request.POST["poliza"]
    poliza.asegurado = request.POST["asegurado"].upper()
    poliza.CUIT = request.POST["CUIT"]
    poliza.fecha = request.POST["fecha"]
    poliza.save()
    return redirect('/')    



def listadoEmpleados(request,id):
    #buscar por id poliza los datos de la poliza y los empleados en el listado
    poliza = Poliza.objects.get(id=id)
    empleados = Empleado.objects.filter(id_poliza_id=id)
    
    return render(request, 'listadoEmpleados.html',{
        'poliza': poliza,
        'empleados': empleados
    })


def edicionEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    
    return render(request, 'edicionEmpleado.html', {
        'empleado': empleado
    })

def editarEmpleado(request, id, id_poliza):
    """Recibe los datos del formulario de edicion de empleado y los actualiza en la base de datos.

    Args:
        request: Objeto request que trae los datos del formulario
        id: ID del empleado a editar
        id_poliza: ID de la poliza a la que pertenece el empleado

    Returns:
        Una redireccion a la pagina de listado de empleados de la poliza.
    """
    nombre = request.POST["nombre"].upper()
    CUIL = request.POST["CUIL"]
    Empleado.objects.filter(id=id).update(
        nombre=nombre,
        CUIL=CUIL
    )
    return redirect(f'/listadoEmpleados/{id_poliza}')

def registrarEmpleado(request,id_poliza):
    """Recibe los datos del formulario de registro de empleado y los guarda en la base de datos.

    Args:
        request: Objeto request que trae los datos del formulario
        id_poliza: ID de la poliza a la que pertenece el empleado

    Returns:
        Una redireccion a la pagina de listado de empleados de la poliza.
    """
    nombre = request.POST["nombre"].upper()
    CUIL = request.POST["CUIL"]
    # crear un nuevo objeto Empleado con los datos recibidos y relacionarlo con la poliza por su ID
    Empleado.objects.create(
        nombre=nombre,
        CUIL=CUIL,
        id_poliza_id=id_poliza
    )
    return redirect(f'/listadoEmpleados/{id_poliza}')

def eliminarEmpleado(request, id, id_poliza):
    Empleado.objects.filter(id=id).delete()
    return redirect(f'/listadoEmpleados/{id_poliza}')

def eliminacionPoliza(request, id):
    Poliza.objects.filter(id=id).delete()
    return redirect('/')
