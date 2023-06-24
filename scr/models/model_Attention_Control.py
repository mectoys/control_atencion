from scr.database.dbconnect import get_connection


class model_Attention_Control:

    @classmethod
    # Listar
    def get_attention_control_list(cls):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL = "SELECT ID, FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK" \
                  " FROM  Attention_Control"
            cursor.execute(SQL)
            listattention_ctrl = cursor.fetchall()
        connection.close()
        # print(listattention_ctrl)
        return listattention_ctrl

    # Insertar
    @classmethod
    def add_attention_control(cls, attention_control):
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
    @classmethod
    def update_attention_control(cls, attention_control):
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

    @classmethod
    def delete_attention_control(cls, id):
        with get_connection() as connection, connection.cursor() as cursor:
            SQL_DELETE = "DELETE FROM Attention_Control WHERE ID = %s"
            cursor.execute(SQL_DELETE, (id,))
            affected_rows =cursor.rowcount
            #confirmar cambios
            connection.commit()
        return affected_rows
    #crud
