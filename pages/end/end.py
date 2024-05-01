import copy

from flask import Blueprint, session, render_template, redirect

# endpage blueprint definition
end = Blueprint('end',
                     __name__,
                     static_folder='static',
                     static_url_path='/end',
                     template_folder='templates')


# Routes
#loud the end/order property
@end.route('/end')
def endpage():
    if (not 'id' in session or not 'name' in session or not 'time' in session or not 'pay' in session): return (redirect('/'))
    order = copy.deepcopy(session)
    return render_template('end.html',order = order)