import psycopg2

def borrarFunciones (connection):
    cursor = connection.cursor()

    funciones = ['check_Mayoria_Edad', 'existe_empleado_tarea', 'borrar_tareas_empleado',
                'check_Fecha_Itinerario', 'existe_empleado_actividad', 'existe_actividad_asistente',
                'borrar_pago_cliente', 'existe_cliente_promocion', 'borrar_cliente_promocion']

    # Consulta para borrar la función
    for funcion in funciones:
        consulta_borrar_funcion = f"DROP FUNCTION IF EXISTS {funcion}() CASCADE;"

        # Ejecutar la consulta
        cursor.execute(consulta_borrar_funcion)

    # Confirmar los cambios en la base de datos
    connection.commit()

    # Cerrar el cursor y la conexión
    cursor.close()

def borrarDisparadores(connection, tabla):

    cursor = connection.cursor()
    cursor.execute(f"SELECT tgname FROM pg_trigger WHERE tgrelid = '{tabla}'::regclass;")
    triggers = cursor.fetchall()

    # Borrar cada trigger
    for trigger in triggers:
        cursor.execute(f"DROP TRIGGER IF EXISTS {trigger[0]} ON {tabla};")

    # Confirmar los cambios en la base de datos
    connection.commit()
    cursor.close()

def crearDisparadores(connection):

    cursor = connection.cursor()

    # Trigger para comprobar si el empleado es mayor de edad
    trigger1 = """CREATE FUNCTION check_Mayoria_Edad()
        RETURNS TRIGGER AS
        $$
        BEGIN
            IF (NEW.FechaNacimiento > (CURRENT_DATE - INTERVAL '18 years')) THEN
                RAISE EXCEPTION 'El empleado debe ser mayor de edad:';
            END IF;
            RETURN NEW;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'validaredad' and tgrelid = 'Empleado'::regclass
            )
            THEN
                CREATE TRIGGER validarEdad
                BEFORE INSERT OR UPDATE ON Empleado
                FOR EACH ROW
                EXECUTE FUNCTION check_Mayoria_Edad();
            END IF;
        END $$;
        """

    cursor.execute(trigger1)

    # Trigger para comprobar si el empleado existe antes de insertar una tarea


    trigger2 = """CREATE FUNCTION existe_empleado_tarea()
        RETURNS TRIGGER AS
        $$
        BEGIN
            IF (NEW.DNI NOT IN (SELECT DNI FROM Empleado)) THEN
                RAISE EXCEPTION 'El empleado no existe';
            END IF;
            RETURN NEW;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'validarempleadotarea' and tgrelid = 'TareaEmpleado'::regclass
            )
            THEN
                CREATE TRIGGER validarEmpleadoTarea
                BEFORE INSERT OR UPDATE ON TareaEmpleado
                FOR EACH ROW
                EXECUTE FUNCTION existe_empleado_tarea();
            END IF;
        END $$;
        """

    cursor.execute(trigger2)

    # Trigger para eliminar las tareas de un empleado cuando se le da de baja
    trigger3 = """CREATE FUNCTION borrar_tareas_empleado()
        RETURNS TRIGGER AS
        $$
        BEGIN
            DELETE FROM TareaEmpleado WHERE DNI = OLD.DNI;
            RETURN OLD;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'eliminartareasempleado' and tgrelid = 'Empleado'::regclass
            )
            THEN
                CREATE TRIGGER eliminarTareasEmpleado
                BEFORE DELETE ON Empleado
                FOR EACH ROW
                EXECUTE FUNCTION borrar_tareas_empleado();
            END IF;
        END $$;
    """

    cursor.execute(trigger3)

    # Trigger para comprobar si la fecha actual es mayor que la fecha del itinerario en 2 días
    trigger4 = """CREATE FUNCTION check_Fecha_Itinerario()
        RETURNS TRIGGER AS
        $$
        BEGIN
            IF (NEW.FechaInicio < (CURRENT_DATE + INTERVAL '2 days')) THEN
                RAISE EXCEPTION 'La fecha del itinerario debe ser al menos 2 días después de la fecha actual';
            END IF;
            RETURN NEW;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'validarfechaitinerario' and tgrelid = 'Itinerario'::regclass
            )
            THEN
                CREATE TRIGGER validarFechaItinerario
                BEFORE INSERT OR UPDATE ON Itinerario
                FOR EACH ROW
                EXECUTE FUNCTION check_Fecha_Itinerario();
            END IF;
        END $$;
    """

    cursor.execute(trigger4)

    # Trigger para comprobar si el empleado existe antes de crear una actividad
    trigger5 = """CREATE FUNCTION existe_empleado_actividad()
        RETURNS TRIGGER AS
        $$
        BEGIN
            IF (NEW.DNI NOT IN (SELECT DNI FROM Empleado)) THEN
                RAISE EXCEPTION 'El empleado no existe';
            END IF;
            RETURN NEW;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'validarempleadoactividad' and tgrelid = 'OrganizaActividad'::regclass
            )
            THEN
                CREATE TRIGGER validarEmpleadoActividad
                BEFORE INSERT OR UPDATE ON OrganizaActividad
                FOR EACH ROW
                EXECUTE FUNCTION existe_empleado_actividad();
            END IF;
        END $$;
    """

    cursor.execute(trigger5)

    # Trigger para comprobar si la actividad existe antes de añadir un asistente
    trigger6 = """CREATE FUNCTION existe_actividad_asistente()
        RETURNS TRIGGER AS
        $$
        BEGIN
            IF (NEW.Fecha NOT IN (SELECT Fecha FROM OrganizaActividad WHERE Nombre = NEW.Nombre)) THEN
                RAISE EXCEPTION 'La actividad no existe';
            END IF;
            RETURN NEW;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'validaractividadasistente' and tgrelid = 'AsisteActividad'::regclass
            )
            THEN
                CREATE TRIGGER validarActividadAsistente
                BEFORE INSERT OR UPDATE ON AsisteActividad
                FOR EACH ROW
                EXECUTE FUNCTION existe_actividad_asistente();
            END IF;
        END $$;
    """

    cursor.execute(trigger6)

    # Trigger para borrar el pago asocialdo a un cliente cuando se realiza un reembolso
    trigger7 = """CREATE FUNCTION borrar_pago_cliente()
        RETURNS TRIGGER AS
        $$
        BEGIN
            DELETE FROM PagoCliente WHERE ID = OLD.ID;
            RETURN OLD;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'eliminarpagocliente' and tgrelid = 'Pago'::regclass
            )
            THEN
                CREATE TRIGGER eliminarPagoCliente
                BEFORE DELETE ON Pago
                FOR EACH ROW
                EXECUTE FUNCTION borrar_pago_cliente();
            END IF;
        END $$;
    """

    cursor.execute(trigger7)

    # Trigger para comprobar si el cliente y la promocion existen antes de añadir una consulta
    trigger8 = """CREATE FUNCTION existe_cliente_promocion()
        RETURNS TRIGGER AS
        $$
        BEGIN
            IF (NEW.DNI NOT IN (SELECT DNI FROM Cliente)) THEN
                RAISE EXCEPTION 'El cliente no existe';
            END IF;
            IF (NEW.ID NOT IN (SELECT ID FROM Promocion)) THEN
                RAISE EXCEPTION 'La promocion no existe';
            END IF;
            RETURN NEW;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'validarclientepromocion' and tgrelid = 'ConsultaPromocion'::regclass
            )
            THEN
                CREATE TRIGGER validarClientePromocion
                BEFORE INSERT OR UPDATE ON ConsultaPromocion
                FOR EACH ROW
                EXECUTE FUNCTION existe_cliente_promocion();
            END IF;
        END $$;
    """

    cursor.execute(trigger8)

    # Trigger para borrar cliente de promocion y de pago cuando se elimina un cliente
    trigger9 = """CREATE FUNCTION borrar_cliente_promocion()
        RETURNS TRIGGER AS
        $$
        BEGIN
            IF EXISTS (SELECT 1 FROM ConsultaPromocion WHERE DNI = OLD.DNI) THEN
                DELETE FROM ConsultaPromocion WHERE DNI = OLD.DNI;
            END IF;
            IF EXISTS (SELECT 1 FROM PagoCliente WHERE DNI = OLD.DNI) THEN
                DELETE FROM PagoCliente WHERE DNI = OLD.DNI;
            END IF;
            RETURN OLD;
        END;
        $$
        LANGUAGE plpgsql;

        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_trigger
                WHERE tgname = 'eliminarclientepromocion' and tgrelid = 'Cliente'::regclass
            )
            THEN
                CREATE TRIGGER eliminarClientePromocion
                BEFORE DELETE ON Cliente
                FOR EACH ROW
                EXECUTE FUNCTION borrar_cliente_promocion();
            END IF;
        END $$;
    """

    cursor.execute(trigger9)


    connection.commit()
    cursor.close()