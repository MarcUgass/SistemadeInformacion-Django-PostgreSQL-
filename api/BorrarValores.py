import psycopg2

def DarBajaEmpleado(connection, dni):

    # Create a cursor
    cursor = connection.cursor()

    delete_query = f"DELETE FROM Empleado WHERE DNI = '{dni}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
    except:
        connection.rollback()
        print("Error al borrar el empleado")
    finally:
        cursor.close()


def DarBajaCliente(connection, dni):

    # Create a cursor
    cursor = connection.cursor()
    delete_query = "DELETE FROM Cliente WHERE DNI = '75941071b'"

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

