import psycopg2
import random

def salarioEmpleado(connection, dni, salario):

    cursor = connection.cursor()
    update_query = f"UPDATE Empleado SET Salario = {salario} WHERE DNI = '{dni}'"
    try:
        cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error actualizando el salario\n")
    finally:
        cursor.close()


def nuevaTarea(connection, dni, tarea, fecha_ini, fecha_fin):

    cursor = connection.cursor()
    insert_query = f"INSERT INTO TareaEmpleado (DNI, Tarea) VALUES ('{dni}', '{tarea}')"
    try:
        cursor.execute(insert_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error insertando la tarea\n")

    update_query = f"UPDATE Empleado SET FechaInicioTarea = '{fecha_ini}', FechaFinTarea = '{fecha_fin}' WHERE DNI = '{dni}'"

    try:
        cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error actualizando las fechas de la tarea\n")

    cursor.close()


def cambioItinerario(connection, id, medio_transporte, fecha_salida, fecha_llegada, origen, destino, precio):

    cursor = connection.cursor()
    update_query = f"UPDATE Itinerario SET MedioTransporte = '{medio_transporte}', FechaSalida = '{fecha_salida}', FechaLlegada = '{fecha_llegada}', Origen = '{origen}', Destino = '{destino}', Precio = '{precio}' WHERE ID = {id}"

    try:
        cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error actualizando el itinerario\n")
    finally:
        cursor.close()


def modificarAsientoBillete(connection, DNI, id, asiento):

    cursor = connection.cursor()
    update_query = f"UPDATE Billete SET Asiento = {asiento} WHERE DNI = '{DNI}' AND ID = {id}"

    try:
        cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error modificando el asiento\n")
    finally:
        cursor.close()


def modificarPuntosInteres(connection, fecha, nombre, puntosDeInteres):

    cursor = connection.cursor()
    update_query = f"UPDATE PuntosDeInteresActividad SET PuntosDeInteres = {puntosDeInteres} WHERE Fecha = '{fecha}' AND Nombre = '{nombre}'"

    try:
        cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error actualizando los puntos de interes\n")
    finally:
        cursor.close()


def modificarPrecioActividad(connection, fecha, nombre, precio):

    cursor = connection.cursor()
    update_query = f"UPDATE UbicacionActividad SET Precio = {precio} WHERE Nombre = '{nombre}' AND Fecha = '{fecha}'"

    try:
        cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error actualizando el precio\n")
    finally:
        cursor.close()


def modificarDatosCliente(connection, dni, nombre, apellidos, fecha_nacimiento, email, telefono):

    cursor = connection.cursor()
    update_query = f"UPDATE Cliente SET Nombre = '{nombre}', Apellidos = '{apellidos}', FechaNacimiento = '{fecha_nacimiento}', Email = '{email}', Telefono = '{telefono}' WHERE DNI = '{dni}'"

    try:
        cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
        print("Ha ocurrido un error actualizando los datos del cliente\n")
    finally:
        cursor.close()
        
def SiguienteIdItinerarioDisponible(connection):
        # Create a cursor
        cursor = connection.cursor()
        existe = True
        # Execute the SELECT statement
        select_query = f"SELECT MAX(ID) FROM Itinerario"
        cursor.execute(select_query)
        comprobacion = cursor.fetchone()[0]
        if(comprobacion == None):
            existe = False
        # Fetch the first row
        row = comprobacion

        # Close the cursor and connection
        cursor.close()
        if(existe == False):
            return 0
        else:
            return row + 1
        
def IdPromocion():
    return random.randint(1,10000000)