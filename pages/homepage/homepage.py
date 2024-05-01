from flask import Blueprint, session, render_template, jsonify, request, redirect

from utilities.db.db_manager import DB_new_order, DB_get_products

# homepage blueprint definition
homepage = Blueprint('homepage',
                     __name__,
                     static_folder='static',
                     static_url_path='/homepage',
                     template_folder='templates')


# Routes


@homepage.route('/homepage')
@homepage.route('/')
def home():

    if (not 'id' in session) or session['page'] == "end":
        session['id'] = DB_new_order()
        session['products'] = []

    session['page'] = 'homepage'
    session['information_error'] = 'none'
    products = DB_get_products()
    return render_template('home_menu.html'
                           , order=session['products']
                           , data_products=products
                           , data_main_products=products)


@homepage.route('/sendOrder', methods=['POST'])
def receive_order():
    if (not 'id' in session): return (redirect('/'))
    data_received = request.json
    print('Data received from client:', data_received)
    session['products'] = data_received[0]
    session['price'] = data_received[1]
    print(session['products'])
    return jsonify({'message': 'Data received successfully', 'data': data_received})

