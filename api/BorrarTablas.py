import psycopg2
import random

def drop(connection):
    Tablas = ["ClaseAsiento", "Billete", "AsisteActividad", "PuntosInteresActividad", "HorarioActividad", 
              "UbicacionActividad", "ActividadViaje", "OrganizaActividad", "ConsultaPromocion", "PagoCliente", 
              "Pago", "Itinerario", "Promocion", "TareaEmpleado", "Empleado", "Cliente"]
    cursor = connection.cursor()

    try:
        for tabla in Tablas:
            delete_query = f"DROP TABLE {tabla}"
            cursor.execute(delete_query)
        print("La base de datos ha sido borrada")
    except:
        print("La base de datos no existía previamente")

    connection.commit()

    # Close the cursor and connection
    cursor.close()


