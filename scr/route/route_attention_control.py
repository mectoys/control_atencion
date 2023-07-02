from flask import Blueprint, render_template, request
from flask_paginate import Pagination, get_page_args

from scr.models.model_Attention_Control import model_Attention_Control

main = Blueprint('attention_ctrl_bp', __name__)


# Select
@main.route('/')
def Index():
    # Obtener los parametros de paginación de la URL actual
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    # Obtener datos  para la tabla
    attentions = model_Attention_Control.get_attention_control_list_ver2()

    data = []
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
        }
        data.append(attention_dict)
        # calcular el numero total de elementos y la lista de elementos para la pag. actual.
        total = len(data)
        paginated_data = attentions[offset: offset + per_page]
        # Crear objeto Pagination
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        # data = model_Attention_Control.get_attention_control_list()

    return render_template('index.html', attentions=paginated_data, pagination=pagination)


# insert
@main.route('/insert', methods=['POST'])
def insert():
    return render_template('index.html')


# update
@main.route('/update', methods=['POST'])
def update():
    return render_template('index.html')


# delete
@main.route('/delete/<string:id>')
def delete(id):
    return render_template('index.html')
