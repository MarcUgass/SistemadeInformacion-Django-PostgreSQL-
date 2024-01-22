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
    contexto = {"tipo0" : "oculto", "tipo1" : "oculto", "tipo2" : "oculto", "tipo3" : "oculto", "tipo4" : "oculto",
                "Clientes0" : "oculto", "Clientes1" : "oculto", "Clientes2" : "oculto", 
                "Itin0" : "oculto", "Itin1" : "oculto",
                "Promo0" : "oculto", "Promo1" : "oculto",
                "Act0" : "oculto", "Act1" : "oculto",
                "Trab0" : "oculto", "Trab1" : "oculto", "Trab2" : "oculto", "Trab3" : "oculto", "Trab4" : "oculto",
                "dni" : "", "first_name" : "", "last_name" : "", "fecha_nacimiento": "", "email" : "", "telefono" : "",
                "salario" : "oculto", "fecha_ini" : "oculto", "fecha_fin" : "oculto"}
    if(request.method == 'POST'):

        connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
        )

        if(request.POST.get('Control',"") == "Clientes"):
            if(request.POST.get('Form',"") == "Consulta"):
                valores = ConsultarExpedienteCliente(request.POST.get("dni",""), connection)
                if(valores != None):
                    contexto['dni'] = valores[0]
                    contexto['first_name'] = valores[1]
                    contexto['last_name'] = valores[2]
                    contexto['fecha_nacimiento'] = valores[3]
                    contexto['email'] = valores[4]
                    contexto['telefono'] = valores[5]
                    contexto['Clientes0'] = ""

            elif(request.POST.get('Form',"") == "Alteracion"):
                try:
                    modificarDatosCliente(connection, request.POST.get("dni",""),request.POST.get("nombre",""),
                                        request.POST.get("apellido",""), request.POST.get("fecha_nacimiento",""),
                                        request.POST.get("correo",""), request.POST.get("telefono",""))
                    contexto['Clientes1'] = ""
                except:
                    print("No se ha podido modificar")
            elif(request.POST.get('Form',"") == "Borrado"):
                DNI = request.POST.get("dni","")
                resultado = DarBajaCliente(connection, DNI)
                if(resultado == 0):
                    contexto['Clientes2'] = ""
                else:
                    print("No se ha podido borrar el cliente")

            contexto['tipo4'] = ""

        elif(request.POST.get('Control',"") == "Itinerarios"):
            if(request.POST.get('Form',"") == "Creación"):
                if(registroItinerario(connection,str(SiguienteIdItinerarioDisponible(connection)),request.POST.get("transporte",""),request.POST.get("fecha_ini",""),
                                   request.POST.get("fecha_fin",""),request.POST.get("origen",""),request.POST.get("destino",""),
                                   request.POST.get("precio","")) == 0):
                    contexto['Itin0'] = ""
                
                
            
            elif(request.POST.get('Form', "") == "Alteracion"):
                if(cambioItinerario(connection,request.POST.get("ID",""),request.POST.get("transporte",""),request.POST.get("fecha_ini",""),
                                   request.POST.get("fecha_fin",""),request.POST.get("origen",""),request.POST.get("destino",""),
                                   request.POST.get("precio","")) == 0):
                    contexto['Itin1'] = ""
                
            contexto['tipo1'] = ""

        elif(request.POST.get('Control',"") == "Actividades"):
            if(request.POST.get('Form',"") == "Creación"):
                if(registroActividad(connection,request.POST.get("dni",""),request.POST.get("fecha",""),request.POST.get("nombre",""),
                                  request.POST.get("hora", ""), request.POST.get("ubi",""), request.POST.get("precio",""), "") == 0):
                    contexto['Act0'] = ""
                
            elif(request.POST.get('Form', "") == "PInteres"):
                if(modificarPuntosInteres(connection,request.POST.get("fecha",""),request.POST.get("nombre",""),request.POST.get("puntos","")) == 0):
                    contexto['Act1'] = ""
                
            contexto['tipo2'] = ""

        elif(request.POST.get('Control',"") == "Promociones"):
            if(request.POST.get('Form',"") == "Creación"):
                try:
                    registroPromocion(connection, SiguienteIdPromocionDisponible(connection), request.POST.get("nombre","" ), request.POST.get("fecha_ini",""), request.POST.get("fecha_fin",""), 
                                    request.POST.get("destino",""), request.POST.get("precio","") )
                    contexto['Promo0'] = ""
                except:
                    print("No se ha podido registrar")



            if (request.POST.get('Form', "") == "devolucion"):
                RealizarDevolucion(connection, request.POST.get("ID",""))
                contexto['Promo1'] = ""
            
            contexto["tipo3"] = ""

        elif(request.POST.get('Control',"") == "Trabajadores"):
            if(request.POST.get('Form',"") == "Creación"):
                if(registroEmpleado(connection,request.POST.get("dni",""),request.POST.get("nombre",""),request.POST.get("apellido",""),
                                request.POST.get("fecha_nacimiento",""), request.POST.get("correo",""), request.POST.get("telefono",""),
                                request.POST.get("fecha_ini",""), request.POST.get("fecha_fin",""), request.POST.get("salario","")) == 0):
                    contexto["Trab0"] = ""

            elif(request.POST.get('Form',"") == "ActSalario"):
                if(salarioEmpleado(connection,request.POST.get("dni",""),request.POST.get("salario","")) == 0):
                    contexto["Trab1"] = ""

            elif(request.POST.get('Form',"") == "ActTarea"):
                if(nuevaTarea(connection,request.POST.get("dni",""),request.POST.get("tarea",""),request.POST.get("fecha_ini",""),request.POST.get("fecha_fin","")) == 0):
                    contexto["Trab2"] = ""

            elif(request.POST.get('Form',"") == "Borrar"):
                if(DarBajaEmpleado(connection,request.POST.get("dni","")) == 0):
                    contexto["Trab3"] = ""

            elif(request.POST.get('Form',"") == "Consulta"):
                valores = ConsultarExpedienteEmpleado(request.POST.get("dni",""),connection)
                if(valores != None):
                    contexto['dni'] = valores[0]
                    contexto['first_name'] = valores[1]
                    contexto['last_name'] = valores[2]
                    contexto['fecha_nacimiento'] = valores[3]
                    contexto['email'] = valores[4]
                    contexto['telefono'] = valores[5]
                    contexto['fecha_ini'] = valores[6]
                    contexto['fecha_fin'] = valores[7]
                    contexto['salario'] = valores[8]
                    contexto["Trab4"] = ""

            contexto["tipo0"] = ""

        if(request.POST.get('ID',"") == "0"):
            print("Gestion Trabajadores")
            contexto["tipo0"] = ""
        if(request.POST.get('ID',"") == "1"):
            print("Gestion Itinerarios")
            contexto["tipo1"] = ""
        if(request.POST.get('ID',"") == "2"):
            print("Gestion Actividades")
            contexto["tipo2"] = ""
        if(request.POST.get('ID',"") == "3"):
            print("Gestion Promociones")
            contexto["tipo3"] = ""
        if(request.POST.get('ID',"") == "4"):
            print("Gestion Clientes")
            contexto["tipo4"] = ""

    return render(request, 'panelcontrol.html', contexto)

