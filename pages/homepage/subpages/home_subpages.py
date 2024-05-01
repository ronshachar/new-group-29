from flask import*  #  Blueprint, render_template, redirect, url_for
from utilities.db.db_manager import DB_get_products, DB_get_drinkProducts, DB_get_toppings, DB_get_defaultTopping

# homepage blueprint definition
home_subpages = Blueprint('home_subpage',
                     __name__,
                     static_folder='static',
                     static_url_path='/subpages',
                     template_folder='templates')


# Routes
@home_subpages.route('/home')
def loudhome():
    return redirect('/')

@home_subpages.route('/home_drinks')
def louddrink():
    if (not 'id' in session): return (redirect('/'))
    return render_template('home_menu.html'
                           ,order = session['products']
                           ,data_products = DB_get_products()
                           ,data_main_products = DB_get_drinkProducts())

@home_subpages.route('/home_hamburger')
def loudhamburger():
    if (not 'id' in session): return (redirect('/'))
    return render_template('hamburger.html',
                           order = session['products'],
                           data_products = DB_get_products(),
                           data_toppings = DB_get_toppings(),
                           data_defaultTopping = DB_get_defaultTopping())
