from scr.database.dbconnect import get_connection


class model_Attention_Control:

    @classmethod
    #Listar
    def get_attention_control_list(cls):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL = "SELECT ID, FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK" \
                  " FROM  Attention_Control"
            cursor.execute(SQL)
            listattention_ctrl = cursor.fetchall()
        connection.close()
        #print(listattention_ctrl)
        return listattention_ctrl
    #Insertar

    @classmethod
    def add_attention_control(cls,attention_control):
        connection =get_connection()
        with connection.cursor()as cursor:
            #SQLINJECTION EVITA CON LA CONSULTA PARAMETRIZADA
            SQLINSERT="INSERT INTO Attention_Control(FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK)"\
                " VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values=(attention_control.fecha, attention_control.nombres, attention_control.hora_ingreso, attention_control.hora_salida,
                    attention_control.polo_gift, attention_control.keychain_gift, attention_control.catalog_book)
            cursor.execute(SQLINSERT,values)
            affected_rows= cursor.rowcount
            connection.commit()
        return affected_rows
