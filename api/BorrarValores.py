import psycopg2

def DarBajaEmpleado(connection, dni):

    # Create a cursor
    cursor = connection.cursor()

    delete_query = f"DELETE FROM Empleado WHERE DNI = '{dni}'"

    result = 0

    try:
        cursor.execute(delete_query)
        connection.commit()
    except:
        connection.rollback()
        print("Error al borrar el empleado")
        result = 1

    finally:
        cursor.close()

    return result

def DarBajaCliente(connection, dni):

    # Create a cursor
    cursor = connection.cursor()
    delete_query = f"DELETE FROM Cliente WHERE DNI = '{dni}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
    except:
        connection.rollback()
        print("Error al borrar el cliente")
        return 1
    finally:
        cursor.close()
    
    return 0

def eliminarItinerario(connection, id):
    # Create a cursor
    cursor = connection.cursor()

    delete_query = f"DELETE FROM Itinerario WHERE ID = {id}"

    try:
        cursor.execute(delete_query)
        connection.commit()
    except:
        connection.rollback()
        print("Error al borrar el itinerario")
    finally:
        cursor.close()



def RealizarDevolucion(connection, id):

    # Create a cursor
    cursor = connection.cursor()

    delete_query = f"DELETE FROM Pago WHERE ID = {id}"

    try:
        cursor.execute(delete_query)
        connection.commit()
    except:
        connection.rollback()
        print("Error al borrar el pago")
    finally:
        cursor.close()

