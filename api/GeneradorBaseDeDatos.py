import psycopg2
def crearBaseDeDatos(connection):

    # Create a cursor
    cursor = connection.cursor()

    # Execute a SQL query

    # Tabla Cliente
    cursor.execute("""CREATE TABLE IF NOT EXISTS Cliente (
        DNI VARCHAR(9) PRIMARY KEY,
        Nombre VARCHAR(15),
        Apellidos VARCHAR(40),
        FechaNacimiento DATE,
        Email VARCHAR(40),
        Telefono NUMERIC(9)
    );""")

    # Tabla Empleado
    cursor.execute("""CREATE TABLE IF NOT EXISTS Empleado (
        DNI VARCHAR(9) PRIMARY KEY,
        Nombre VARCHAR(15),
        Apellidos VARCHAR(40),
        FechaNacimiento DATE,
        Email VARCHAR(40),
        Telefono NUMERIC(9),
        FechaInicioTarea DATE,
        FechaFinTarea DATE CHECK (FechaFinTarea - FechaInicioTarea > 0),
        Salario INT
    );""")

    # Tabla TareaEmpleado
    cursor.execute("""CREATE TABLE IF NOT EXISTS TareaEmpleado (
        DNI VARCHAR(9) PRIMARY KEY,
        Tarea VARCHAR(80)
    );""")

    # Tabla Promoción
    cursor.execute("""CREATE TABLE IF NOT EXISTS Promocion (
        ID INT PRIMARY KEY,
        Nombre VARCHAR(15),
        FechaInicio DATE,
        FechaFin DATE,
        Destino VARCHAR(20),
        Precio INT
    );""")

    # Tabla Itinerario
    cursor.execute("""CREATE TABLE IF NOT EXISTS Itinerario (
        ID INT PRIMARY KEY,
        MedioTransporte VARCHAR(15),
        FechaInicio DATE,
        FechaFin DATE,
        Origen VARCHAR(20),
        Destino VARCHAR(20) CHECK (Origen != Destino),
        Precio INT
    );""")

    # Tabla Pago
    cursor.execute("""CREATE TABLE IF NOT EXISTS Pago (
        ID INT PRIMARY KEY,
        FormaDePago VARCHAR(15),
        Cantidad INT CHECK (Cantidad > 0)
    );""")

    # Tabla PagoCliente
    cursor.execute("""CREATE TABLE IF NOT EXISTS PagoCliente (
        ID INT REFERENCES Pago (ID),
        DNI VARCHAR(9) REFERENCES Cliente (DNI),
        PRIMARY KEY (ID, DNI)
    );""")

    # Tabla ConsultaPromocion
    cursor.execute("""CREATE TABLE IF NOT EXISTS ConsultaPromocion (
        DNI VARCHAR(9) REFERENCES Cliente (DNI),
        ID INT REFERENCES Promocion (ID),
        PRIMARY KEY (DNI, ID)
    );""")

    # Tabla OrganizaActividad
    cursor.execute("""CREATE TABLE IF NOT EXISTS OrganizaActividad (
        DNI VARCHAR(9) REFERENCES Empleado (DNI),
        Fecha DATE,
        Nombre VARCHAR(15),
        CONSTRAINT fechaNombre UNIQUE (Fecha, Nombre),
        PRIMARY KEY (DNI, Fecha, Nombre)
    );""")

    # Tabla ActividadViaje
    cursor.execute("""CREATE TABLE IF NOT EXISTS ActividadViaje (
        ID INT REFERENCES Itinerario (ID),
        Fecha DATE,
        Nombre VARCHAR(15),
        Maletas INT,
        Hotel VARCHAR(20),
        PRIMARY KEY (ID, Fecha, Nombre),
        FOREIGN KEY (Fecha, Nombre) REFERENCES OrganizaActividad (Fecha, Nombre)
    );""")

    # Tabla UbicacionActividad
    cursor.execute("""CREATE TABLE IF NOT EXISTS UbicacionActividad (
        Fecha DATE,
        Nombre VARCHAR(15),
        Ubicacion VARCHAR(20),
        Precio INT,
        PRIMARY KEY (Fecha, Nombre),
        FOREIGN KEY (Fecha, Nombre) REFERENCES OrganizaActividad (Fecha, Nombre)
    );""")

    # Tabla HorarioActividad
    cursor.execute("""CREATE TABLE IF NOT EXISTS HorarioActividad (
        Fecha DATE,
        Nombre VARCHAR(15),
        Horario TIME,
        PRIMARY KEY (Fecha, Nombre),
        FOREIGN KEY (Fecha, Nombre) REFERENCES OrganizaActividad (Fecha, Nombre)
    );""")

    # Tabla PuntosInteresActividad
    cursor.execute("""CREATE TABLE IF NOT EXISTS PuntosInteresActividad (
        Fecha DATE,
        Nombre VARCHAR(15),
        PuntoInteres VARCHAR(20),
        PRIMARY KEY (Fecha, Nombre),
        FOREIGN KEY (Fecha, Nombre) REFERENCES OrganizaActividad (Fecha, Nombre)
    );""")

    # Tabla AsisteActividad
    cursor.execute("""CREATE TABLE IF NOT EXISTS AsisteActividad (
        Fecha DATE,
        Nombre VARCHAR(15),
        DNI VARCHAR(9),
        PRIMARY KEY (Fecha, Nombre),
        FOREIGN KEY (Fecha, Nombre) REFERENCES OrganizaActividad (Fecha, Nombre)
    );""")

    # Tabla ClaseAsiento
    cursor.execute("""CREATE TABLE IF NOT EXISTS ClaseAsiento (
        Asiento INT PRIMARY KEY,
        Clase VARCHAR(15)
    );""")

    # Tabla Billete
    cursor.execute("""CREATE TABLE IF NOT EXISTS Billete (
        DNI VARCHAR(9) REFERENCES Cliente (DNI),
        ID INT REFERENCES Itinerario (ID),
        Asiento INT REFERENCES ClaseAsiento (Asiento),
        PRIMARY KEY (DNI, ID)
    );""")


    connection.commit()

    # Close the cursor and connection
    cursor.close()
