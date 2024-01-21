import psycopg2
import random
from datetime import datetime, timedelta

def registroEmpleado(connection, DNI_empleado, Nombre, Apellido, Fecha_nacimiento, Correo, Telefono,
                            Fecha_ini_tarea, Fecha_fin_tarea, Salario):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO Empleado (DNI, Nombre, Apellidos, FechaNacimiento, Email, Telefono, FechaInicioTarea, FechaFinTarea, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    try:
        cursor.execute(insert_query, (DNI_empleado, Nombre, Apellido, Fecha_nacimiento, Correo, Telefono, Fecha_ini_tarea,
                                    Fecha_fin_tarea, Salario))
        connection.commit()
    except Exception as error:
        connection.rollback()
        print(f"{error}")
    except:
        connection.rollback()
        print("Error al insertar empleado")
    finally:
        cursor.close()


def tareaEmpleado(connection, DNI_empleado, Tarea):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO TareaEmpleado (DNI, Tarea) VALUES (%s, %s)"

    try:
        cursor.execute(insert_query, (DNI_empleado, Tarea))
        connection.commit()
    except psycopg2.InternalError as error:
        connection.rollback()
        print(f"{error}")
    except:
        connection.rollback()
        print("Error al insertar tarea")
    finally:
        cursor.close()


def registroItinerario(connection, ID, MedioTransporte, Fecha_salida, Fecha_llegada, Origen, Destino, Precio):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO Itinerario (ID, MedioTransporte, FechaInicio, FechaFin, Origen, Destino, Precio) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    try:
        cursor.execute(insert_query, (ID, MedioTransporte, Fecha_salida, Fecha_llegada, Origen, Destino, Precio))
        connection.commit()
    except psycopg2.InternalError as error:
        connection.rollback()
        print(f"{error}")
    finally:
        cursor.close()


def registroPromocion(connection, ID, Nombre, Fecha_ini, Fecha_fin, Destino, Precio):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO Promocion (ID, Nombre, FechaInicio, FechaFin, Destino, Precio) VALUES (%s, %s, %s, %s, %s, %s)"

    try:
        cursor.execute(insert_query, (ID, Nombre, Fecha_ini, Fecha_fin, Destino, Precio))
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Error al insertar promocion:  {e}")
    finally:
        cursor.close()


def ClientePromocion(connection, DNI, ID):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO ConsultaPromocion (DNI, ID) VALUES (%s, %s)"

    try:
        cursor.execute(insert_query, (DNI, ID))
        connection.commit()
    except psycopg2.InternalError as error:
        connection.rollback()
        print(f"{error}")
    except:
        connection.rollback()
        print("Error al insertar cliente promocion")
    finally:
        cursor.close()


def registroPago(connection, ID, FormaDePago, Cantidad, DNI):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO Pago (ID, FormaDePago, Cantidad) VALUES (%s, %s, %s)"

    try:
        cursor.execute(insert_query, (ID, FormaDePago, Cantidad))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar pago")

    insert_query = f"INSERT INTO PagoCliente (ID, DNI) VALUES (%s, %s)"

    try:
        cursor.execute(insert_query, (ID, DNI))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar pago cliente")

    cursor.close()


def registroActividadViaje(connection, ID, Fecha, Nombre, num_maletas, HotelDestino):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO ActividadViaje (ID, Fecha, Nombre, Num_maletas, HotelDestino) VALUES (%s, %s, %s, %s, %s)"

    try:
        cursor.execute(insert_query, (ID, Fecha, Nombre, num_maletas, HotelDestino))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar actividad viaje")
    finally:
        cursor.close()


def registroActividad(connection, DNI, Fecha, Nombre, Horario, Ubicacion, Precio, PuntoInteres):

    # Execute a SQL query

    cursor = connection.cursor()

    insert_query_1 = f"INSERT INTO OrganizaActividad (DNI, Fecha, Nombre) VALUES (%s, %s, %s)"
    try:
        cursor.execute(insert_query_1, (DNI, Fecha, Nombre))
        connection.commit()
    except psycopg2.InternalError as error:
        connection.rollback()
        print(f"{error}")
    except:
        connection.rollback()
        print("Error al insertar actividad")

    insert_query_2 = f"INSERT INTO HorarioActividad (Fecha, Nombre, Horario) VALUES (%s, %s, %s)"
    try:
        cursor.execute(insert_query_2, (Fecha, Nombre, Horario))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar horario actividad")

    insert_query_3 = f"INSERT INTO UbicacionActividad (Fecha, Nombre, Ubicacion, Precio) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(insert_query_3, (Fecha, Nombre, Ubicacion, Precio))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar ubicacion actividad")

    insert_query_4 = f"INSERT INTO PuntosInteresActividad (Fecha, Nombre, PuntoInteres) VALUES (%s, %s, %s)"
    try:
        cursor.execute(insert_query_4, (Fecha, Nombre, PuntoInteres))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar punto interes actividad")

    cursor.close()


def registroAsistenteActividad(connection, Fecha, Nombre, DNI):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO AsisteActividad (Fecha, Nombre, DNI) VALUES (%s, %s, %s)"

    try:
        cursor.execute(insert_query, (Fecha, Nombre, DNI))
        connection.commit()
    except psycopg2.InternalError as error:
        connection.rollback()
        print(f"{error}")
    except:
        connection.rollback()
        print("Error al insertar asistente actividad")
    finally:
        cursor.close()


def registroCliente(connection, DNI, Nombre, Apellidos, FechaNacimiento, Email, Telefono):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO Cliente (DNI, Nombre, Apellidos, FechaNacimiento, Email, Telefono) VALUES (%s, %s, %s, %s, %s, %s)"

    try:
        cursor.execute(insert_query, (DNI, Nombre, Apellidos, FechaNacimiento, Email, Telefono))
        connection.commit()
    except psycopg2.IntegrityError:
        connection.rollback()
        print("Error al insertar cliente")
        cursor.close()
        return 1
    except psycopg2.DataError:
        cursor.close()
        return 2

    return 0

def registroBillete(connection, DNI, idItinierario, Asiento):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO Billete (DNI, idItinierario, Asiento) VALUES (%s, %s, %s)"

    try:
        cursor.execute(insert_query, (DNI, idItinierario, Asiento))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar billete")
    finally:
        cursor.close()


def definirClaseAsiento (connection, Asiento, Clase):

    # Execute a SQL query
    cursor = connection.cursor()
    insert_query = f"INSERT INTO ClaseAsiento (Asiento, Clase) VALUES (%s, %s)"

    try:
        cursor.execute(insert_query, (Asiento, Clase))
        connection.commit()
    except:
        connection.rollback()
        print("Error al insertar clase asiento")
    finally:
        cursor.close()
