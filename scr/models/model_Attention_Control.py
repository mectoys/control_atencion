from scr.database.dbconnect import get_connection


class model_Attention_Control:

    @classmethod
    def get_attention_control_list(cls):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL = "SELECT ID, FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK" \
                  " FROM  Attention_Control"
            cursor.execute(SQL)
            listattention_ctrl = cursor.fetchall()
        connection.close()
        print(listattention_ctrl)
        return listattention_ctrl
