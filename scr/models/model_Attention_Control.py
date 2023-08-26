from scr.database.dbconnect import get_connection
from datetime import datetime, time


class model_Attention_Control:

    #    @classmethod :Permite acceder y modificar los atributos de la clase.
    # @staticmethod : No puede acceder ni modificar los atributos de instancia o clase , no recibe referecia self, cls

    @staticmethod
    # Listar
    # Para prevenir la inyección de SQL, es recomendable utilizar consultas parametrizadas o consultas preparadas.
    # Estas técnicas permiten separar claramente los datos de la consulta SQL,
    # evitando así la posibilidad de que los datos ingresados por el usuario se interpreten como parte del código SQL.

    def get_attention_control_list():
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT ID, FECHA, NOMBRES, TIME_FORMAT(HORA_INGRESO, '%h:%i %p')  as HORA_INGRESO, " \
                         " TIME_FORMAT(HORA_SALIDA, '%h:%i %p') as HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, CATALOG_BOOK" \
                         " FROM  Attention_Control WHERE STATE ='ACT'"
            cursor.execute(SQL_SELECT)
            listattention_ctrl = cursor.fetchall()

        return listattention_ctrl

    @staticmethod
    # Listar

    def get_attention_control_list_ver2(desde, hasta):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT ID, FECHA, NOMBRES, TIME_FORMAT(HORA_INGRESO, '%h:%i %p') as HORA_INGRESO, " \
                         " TIME_FORMAT(HORA_SALIDA, '%h:%i %p') as  HORA_SALIDA, POLO_GIFT, KEYCHAIN_GIFT, " \
                         "CATALOG_BOOK,HORA_INGRESO as HORA_INGRESO_BD ,HORA_SALIDA AS HORA_SALIDA_BD" \
                         " FROM Attention_Control WHERE STATE ='ACT' AND FECHA >= %s AND FECHA <= %s  ORDER BY FECHA"

            values = (desde, hasta)
            cursor.execute(SQL_SELECT, values)
            result = cursor.fetchall()
            data = []
            for row in result:
                attention_control = model_Attention_Control()
                attention_control.id = row[0]
                attention_control.fecha = row[1]
                attention_control.nombres = row[2]
                # Convertir timedelta a datetime
                attention_control.hora_ingreso = row[3]
                attention_control.hora_salida = row[4]
                attention_control.polo_gift = row[5]
                attention_control.keychain_gift = row[6]
                attention_control.catalog_book = row[7]
                attention_control.hora_ingreso_bd = datetime.strptime(str(row[8]), '%H:%M:%S').time()
                attention_control.hora_salida_bd = datetime.strptime(str(row[9]), '%H:%M:%S').time()

                data.append(attention_control)
        return data

    # Insertar
    @staticmethod
    def add_attention_control(attention_control):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()
        state = 'ACT'
        # SQLINJECTION EVITA CON LA CONSULTA PARAMETRIZADA
        SQL_INSERT = "INSERT INTO Attention_Control(FECHA, NOMBRES, HORA_INGRESO, HORA_SALIDA, POLO_GIFT, " \
                     "KEYCHAIN_GIFT, CATALOG_BOOK, STATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (attention_control.fecha, attention_control.nombres, attention_control.hora_ingreso,
                  attention_control.hora_salida,
                  attention_control.polo_gift, attention_control.keychain_gift, attention_control.catalog_book, state)
        try:
            mi_cursor.execute(SQL_INSERT, values)
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

        # Actualizar

    @staticmethod
    # En este código, se utilizan marcadores de posición %s en la consulta SQL para indicar dónde se deben
    # insertar los valores. Luego, los valores reales se pasan como una tupla separada (values) en el método execute().
    # Esto garantiza que los valores se traten de forma segura y evita la posibilidad de inyección de SQL.
    def update_attention_control(attention_control):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()
        # El bloque with se asegura de que la conexión se cierre correctamente al finalizar,
        # incluso si ocurren excepciones.
        SQLUPDATE = "UPDATE Attention_Control SET FECHA=%s, NOMBRES=%s, HORA_INGRESO=%s, HORA_SALIDA=%s, POLO_GIFT=%s," \
                    " KEYCHAIN_GIFT=%s, CATALOG_BOOK=%s WHERE ID=%s"
        values = (attention_control.fecha, attention_control.nombres, attention_control.hora_ingreso,
                  attention_control.hora_salida,
                  attention_control.polo_gift, attention_control.keychain_gift, attention_control.catalog_book,
                  attention_control.id)
        try:
            mi_cursor.execute(SQLUPDATE, values)
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

    # Eliminar primer enfoque
    @staticmethod
    def delete_attention_control(id):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()

        SQL_DELETE = "DELETE FROM Attention_Control WHERE ID = %s"
        try:
            mi_cursor.execute(SQL_DELETE, (id,))
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

    # Segundo enfoque de Anulacion
    @staticmethod
    def cancel_attention_control(id):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()

        SQL_CANCEL = "UPDATE Attention_Control SET STATE=%s WHERE ID=%s"
        try:
            mi_cursor.execute(SQL_CANCEL, ('ANU', id))
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

    # crud
