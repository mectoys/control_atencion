from scr.database.dbconnect import get_connection


class model_Attention_Control:

    #    @classmethod :Permite acceder y modificar los atributos de la clase.
    # @staticmethod : No puede acceder ni modificar los atributos de instancia o clase , no recibe referecia self, cls

    @staticmethod
    # Listar
    def get_attention_control_list():
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT ID, FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK" \
                         " FROM  Attention_Control"
            cursor.execute(SQL_SELECT)
            listattention_ctrl = cursor.fetchall()

        return listattention_ctrl

    @staticmethod
    # Listar
    def get_attention_control_list_ver2():
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT ID, FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK" \
                         " FROM Attention_Control"
            cursor.execute(SQL_SELECT)
            result = cursor.fetchall()
            data = []
            for row in result:
                attention_control = model_Attention_Control()
                attention_control.id = row[0]
                attention_control.fecha = row[1]
                attention_control.nombres = row[2]
                attention_control.hora_ingreso = row[3]
                attention_control.hora_salida = row[4]
                attention_control.polo_gift = row[5]
                attention_control.keychain_gift = row[6]
                attention_control.catalog_book = row[7]
                data.append(attention_control)
        return data

    # Insertar
    @staticmethod
    def add_attention_control(attention_control):
        connection = get_connection()
        with connection.cursor() as cursor:
            # SQLINJECTION EVITA CON LA CONSULTA PARAMETRIZADA
            SQLINSERT = "INSERT INTO Attention_Control(FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK)" \
                        " VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (attention_control.fecha, attention_control.nombres, attention_control.hora_ingreso,
                      attention_control.hora_salida,
                      attention_control.polo_gift, attention_control.keychain_gift, attention_control.catalog_book)
            cursor.execute(SQLINSERT, values)
            affected_rows = cursor.rowcount
            connection.commit()
        return affected_rows

        # Actualizar

    @staticmethod
    def update_attention_control(attention_control):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQLUPDATE = "UPDATE Attention_Control SET FECHA=%s, NOMBRES=%s, HORA_INGRESO=%s, HORA_SALIDA=%s, POLO_GIFT=%s," \
                        " KEYCHAIN_GIFT=%s, CATALOG_BOOK=%s WHERE ID=%s"
            values = (attention_control.fecha, attention_control.nombres, attention_control.hora_ingreso,
                      attention_control.hora_salida,
                      attention_control.polo_gift, attention_control.keychain_gift, attention_control.catalog_book,
                      attention_control.id)
            cursor.execute(SQLUPDATE, values)
            connection.commit()

    # Eliminar

    @staticmethod
    def delete_attention_control(id):
        with get_connection() as connection, connection.cursor() as cursor:
            SQL_DELETE = "DELETE FROM Attention_Control WHERE ID = %s"
            cursor.execute(SQL_DELETE, (id,))
            affected_rows = cursor.rowcount
            # confirmar cambios
            connection.commit()
        return affected_rows
    # crud
