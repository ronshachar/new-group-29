from flask import *
from utilities.db.db_manager import DB_get_free_tims, DB_is_free_time, DB_reels_time, DB_seize_time

# time page blueprint definition
time = Blueprint('time',
                 __name__,
                 static_folder='static',
                 static_url_path='/time',
                 template_folder='templates')


# Routes

############   time page  ############

###### open time page
@time.route("/Time")
def open_Time():
    if (not session['page'] == 'time'): return (redirect('/'))
    return render_template('time.html',
                           times=DB_get_free_tims(),
                           orderNumber=request.args.get('orderNumber'))


###### receive time data


@time.route('/sendTime', methods=['POST'])
def receive_Time():
    if (not session['page'] == 'time'): return (redirect('/'))
    time = request.json
    success = DB_is_free_time(time)
    if success:
        if 'time' in session.keys():
            DB_reels_time(session['time'])
        session['time'] = time
        DB_seize_time(time)
        session['page'] = 'pay'
    return jsonify({'success': success})
