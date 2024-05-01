from flask import *

from utilities.db.db_manager import DB_insert_order

# pay blueprint definition
pay = Blueprint('pay',
                __name__,
                static_folder='static',
                static_url_path='/pay',
                template_folder='templates')


# Routes

############   pay page  ############

###### open pay page
@pay.route("/pay" )
def open_pay():
    if (not session['page'] == 'pay'): return (redirect('/'))
    return render_template('pay.html',
                           orderNumber=request.args.get('orderNumber')
                           )


###### receive pay data
@pay.route('/sendPay', methods=['POST'])
def receive_Pay():
    if (not session['page'] == 'pay'): return (redirect('/'))
    session['pay'] = request.json['pay']

    DB_insert_order(session)
    session['page'] = "end"
    return redirect('/end')
