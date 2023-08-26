import io

from flask import Blueprint, render_template, request, url_for, make_response, session
from flask_paginate import Pagination, get_page_args
from werkzeug.utils import redirect
import pandas as pd
from scr.models.model_Attention_Control import model_Attention_Control
from scr.models.entities.Attention_Control import Attention_Control

main = Blueprint('attention_ctrl_bp', __name__)


# En este caso, se ha creado la función(auxiliar) get_attention_control_data_from_request() que se encarga
# de procesar los datos comunes de la solicitud. Luego, en cada ruta, se llama a esta función para obtener
# los datos y se utiliza para crear la instancia del modelo o para realizar la actualización en la base de datos.

# De esta manera, se evita la repetición de código y se mantiene el flujo de procesamiento de datos de manera más
# organizada.

# Funcion auxiliar
def get_attention_control_data_from_request():
    fecha = request.form['fecha']
    nombres = request.form['nombres']
    hora_ingreso = request.form['hora_ingreso']
    hora_salida = request.form['hora_salida']
    estado_polo = request.form.get('polo_gift', False)

    if estado_polo == 'on':
        estado_polo = True
    else:
        estado_polo = False

    estado_keychain = request.form.get('keychain_gift', False)

    if estado_keychain == 'on':
        estado_keychain = True
    else:
        estado_keychain = False

    catalog_book = request.form['catalog_book']

    return fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book


# Select
@main.route('/', methods=['GET', 'POST'])
def Index():
    paginated_data = []
    data = []
    pagination = None

    # Obtener los parametros de paginación de la URL actual
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    fecha_desde = session.get('fecha_desde')
    fecha_hasta = session.get('fecha_hasta')

    if request.method == 'POST':
        fecha_desde = request.form.get('fecha_desde')
        fecha_hasta = request.form.get('fecha_hasta')
        session['fecha_desde'] = fecha_desde
        session['fecha_hasta'] = fecha_hasta

    # Obtener datos  para la tabla
    attentions = model_Attention_Control.get_attention_control_list_ver2(fecha_desde, fecha_hasta)

    # convertir los obj. a una lista de diccionario
    for attention in attentions:
        attention_dict = {
            'id': attention.id,
            'fecha': attention.fecha,
            'nombres': attention.nombres,
            'hora_ingreso': attention.hora_ingreso,
            'hora_salida': attention.hora_salida,
            'polo_gift': attention.polo_gift,
            'keychain_gift': attention.keychain_gift,
            'catalog_book': attention.catalog_book,
            'hora_ingreso_bd': attention.hora_ingreso_bd,
            'hora_salida_bd': attention.hora_salida_bd

        }
        data.append(attention_dict)
        # calcular el numero total de elementos y la lista de elementos para la pag. actual.
        total = len(data)
        paginated_data = attentions[offset: offset + per_page]
        # Crear objeto Pagination
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        # data = model_Attention_Control.get_attention_control_list()

    return render_template('index.html', fecha_desde=fecha_desde, fecha_hasta=fecha_hasta,
                           attentions=paginated_data, pagination=pagination)


# insert
@main.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        # obtener los datos comunes de la solicitud
        fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book \
            = get_attention_control_data_from_request()

        retorno = model_Attention_Control.add_attention_control(
            Attention_Control(fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book))

        if retorno == 1:
            print('Registrado')
        else:
            print('No registrado')

            # redirect= funcion que redirige a una URL  especifica.
            # url_for =  funcion que genera la URL para una ruta especifica en función de su nombre.
            # attention_ctrl_bp nombre  de la ruta a la que se va a redirigir.
        return redirect(url_for('attention_ctrl_bp.Index'))


# update
@main.route('/update', methods=['POST'])
def update():
    if request.method == "POST":

        fecha, nombres, hora_ingreso, hora_salida, estado_polo, estado_keychain, catalog_book \
            = get_attention_control_data_from_request()

        idKey = request.form['id']
        attention_control_model = Attention_Control(fecha, nombres, hora_ingreso, hora_salida, estado_polo,
                                                    estado_keychain, catalog_book, idKey)

        retorno = model_Attention_Control.update_attention_control(attention_control_model)
        if retorno == 1:
            print('Actualizado')
        else:
            print('No Actualizado')

        return redirect(url_for('attention_ctrl_bp.Index'))


# delete primer enfoque
@main.route('/delete/<string:id>')
def delete(id):
    retorno = model_Attention_Control.delete_attention_control(id)
    if retorno == 1:
        print('Eliminado')
    else:
        print('No Eliminado')

    return redirect(url_for('attention_ctrl_bp.Index'))


# Anulación segundo enfoque
@main.route('/cancel/<string:id>')
def cancel(id):
    retorno = model_Attention_Control.cancel_attention_control(id)
    if retorno == 1:
        print('Anulado')
    else:
        print('No Anulado')

    return redirect(url_for('attention_ctrl_bp.Index'))


# Exportar Excel
@main.route('/export-excel')
def export_excel():
    # obtener los datos

    attentions = model_Attention_Control.get_attention_control_list()
    df = pd.DataFrame(attentions)

    df = df.rename(columns={0: 'ID', 1: 'FECHA', 2: 'NOMBRES', 3: 'HORA_INGRESO', 4: 'HORA_SALIDA', 5: 'POLO_GIFT',
                            6: 'KEYCHAIN_GIFT', 7: 'CATALOG_BOOK'})

    # Crear un objeto BytesIO para almacenar el excel file en memoria

    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)

    # Explicar que despues de attechment va un punto y coma para arreglar el nombre de la descarga!!!!!
    # response = make_response(buffer.getvalue())
    # response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    #   response.headers['Content-Disposition'] = 'attachment: filename=registros.xlsx'

    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename=registros.xlsx'

    return response
