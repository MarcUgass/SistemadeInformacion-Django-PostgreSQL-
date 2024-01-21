import psycopg2

def imprimirBasesDeDatos(connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute a SQL query to list all tables in the database
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

    # Fetch all the results
    tables = cursor.fetchall()

    # Print the list of table names
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Close the cursor and connection
    cursor.close()

def imprimirValoresDeTablas(connection):
    # Connect to the database
    cursor = connection.cursor()

    Tablas = ["Stock", "Pedido", "Detalle_Pedido"]

    for tabla in Tablas:

        # Execute the SELECT statement to retrieve all values
        select_query = f"SELECT * FROM {tabla}"
        cursor.execute(select_query)

        # Fetch all rows
        rows = cursor.fetchall()

        print(f"\nTabla {tabla}:")

        # Print the results
        for row in rows:
            print(row)

    print ("\n")
    # Close the cursor and the database connection
    cursor.close()

def ConsultarExpedienteEmpleado(dni, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM Empleado WHERE DNI = '{dni}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    print(row)

    # Close the cursor and connection
    cursor.close()
    return row

def ConsultarExpedienteCliente(dni, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM Cliente WHERE DNI = '{dni}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarInformacionItinerario(id, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM Itinerario WHERE ID = '{id}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    # Print the row
    print(row)

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarPromocionesCliente(dni, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM Promocion WHERE ConsultaPromocion = '{dni}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarInfoOrganizaActividades(dni, nombre, fecha, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM OrganizaActividad WHERE DNI = '{dni}' AND Nombre = '{nombre}' AND Fecha = '{fecha}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarInfoActividadViaje(ID, nombre, Fecha, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM ActividadViaje WHERE ID = '{ID}' AND Nombre = '{nombre}' AND Fecha = '{Fecha}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarInfoUbicacionActividad(Nombre, Fecha, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM UbicacionActividad WHERE Nombre = '{Nombre}' AND Fecha = '{Fecha}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarInfoHorarioActividad(Nombre, Fecha, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM HorarioActividad WHERE Nombre = '{Nombre}' AND Fecha = '{Fecha}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarInfoPuntosInteresActividad(Nombre, Fecha, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM PuntosInteresActividad WHERE Nombre = '{Nombre}' AND Fecha = '{Fecha}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    return row

def MostrarInfoAsisteActividad(Nombre, Fecha, connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SELECT statement
    select_query = f"SELECT * FROM AsisteActividad WHERE Nombre = '{Nombre}' AND Fecha = '{Fecha}'"
    cursor.execute(select_query)

    # Fetch the first row
    row = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    return row

