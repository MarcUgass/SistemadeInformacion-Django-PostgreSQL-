from django.shortcuts import render, redirect
from api.GeneradorBaseDeDatos import *
from api.BorrarTablas import *
from api.BorrarValores import *
from api.ComprobarBasesDeDatos import *
from api.AniadirValores import * 
from api.Disparadores import *
from api.ActualizarTablas import * 

# Create your views here.
def index(request):
    if request.method == 'POST':
        request.session['dni'] = ""
    elif(request.session.get('dni', "") != ""):
        return redirect(reservas)
    return render(request, 'index.html')

def inicioSesion(request):
    if request.method == "POST":
        connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
        )

        nombre = request.POST.get("username", "")
        
        if(ConsultarExpedienteCliente(nombre, connection) != None):
            contexto = {"Mensaje_error" : ""}
            request.session['dni'] = nombre
            request.session['modificando'] = ""
            return redirect(reservas)
        else:
            contexto = {"Mensaje_error" : "El usuario o la contraseña no son correctos"}
            return render(request, 'iniciar_sesion.html', contexto)

    else:
        contexto = {"Mensaje_error" : f"{request.session.get('mensajeActual', None)}"}
        request.session['mensajeActual'] = ""
        return render(request, 'iniciar_sesion.html', contexto)

def registro(request):
    if request.method == "POST":
        connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
        )

        resultado = registroCliente(connection,request.POST.get("dni",""),request.POST.get("nombre",""),request.POST.get("apellido",""),request.POST.get("fecha_nacimiento",""),
                        request.POST.get("correo",""),request.POST.get("telefono",""))

        if(resultado == 0):
            request.session['dni'] = request.POST.get("dni","")
            request.session['modificando'] = ""
            return redirect(reservas)
        elif(resultado == 1):
            request.session['mensajeActual'] = "El usuario que intentas registrar ya existe"
            return redirect(inicioSesion)
        else:
            return render(request, 'registro_cliente.html', {"Mensaje_error" : "El formato de alguno de los valores es incorrecto"})
    else:
        return render(request, 'registro_cliente.html')

def baseDeDatos(request):
    return render(request, 'BD-html')

def generarBaseDeDatos(request):

    connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
    )

    connection.autocommit = False

    crearBaseDeDatos(connection)

    borrarDisparadores(connection)
    crearDisparadores(connection)

    connection.close()

    contexto = {
        "miTexto" : "Base de datos actualizada",
    }

    return render(request, 'index.html')

def perfil(request):

    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    if request.POST.get("mod", "") == "2":
        print("Hola")
        request.session['modificando'] = ""
        return redirect('perfil')
    
    if(request.method == 'POST' or request.session.get("modificando","") == "1"):
        if(request.POST.get("nombre", "") == ""):
            request.session['modificando'] = "1"
        else:
            try:
                modificarDatosCliente(connection, request.session.get("dni",""),request.POST.get("nombre",""),
                                      request.POST.get("apellido",""), request.POST.get("fecha_nacimiento",""),
                                      request.POST.get("correo",""), request.POST.get("telefono",""))
                request.session['modificando'] = ""
                return redirect('perfil')
            except:
                print("No se ha podido modificar")
        return render(request, 'modificar_perfil.html')
    else:
        valores = ConsultarExpedienteCliente(request.session.get("dni",""), connection)
        if(valores == None):
            request.session['mensajeActual'] = 'DNI inválido'
            return redirect(inicioSesion)
        contexto = {'dni' : valores[0], 'first_name' : valores[1], 'last_name' : valores[2],
                    'fecha_nacimiento' : valores[3], 'email' : valores[4], 'telefono' : valores[5]}

        return render(request, 'perfil_cliente.html', contexto)
    
def reservas(request):
    request.session['modificando'] = ""
    return render(request, 'reservas_actividades.html')