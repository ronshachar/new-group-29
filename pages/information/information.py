from flask import session, render_template, redirect, request, Blueprint

# homepage blueprint definition
information = Blueprint('information',
                        __name__,
                        static_folder='static',
                        static_url_path='/information',
                        template_folder='templates')


# Routes

############   information page  ############

###### open information page
@information.route("/information")
def open_Information():
    if (session['page'] == 'homepage'):
        session['page'] = "information"
    if (not session['page'] == 'information'): return (redirect('/'))
    if 'name' in session:
        return render_template('information.html',
                               orderNumber=session.get('id'),
                               name=session['name'],
                               phone=session['phone'],
                               error = session['information_error'] )

    else:
        return render_template('information.html',
                               orderNumber=session.get('id'))


# allow to continue only all the field are valid
def valid_sand():
    if session['name'] == '':
        session['information_error'] = 'the name is empty'
        return False

    if (not len(session['phone']) == 10):
        session['information_error'] = 'invalid phone number'
        return False

    return True


###### receive information data
@information.route('/sendData', methods=['POST'])
def receive_data():
    if (not session['page'] == 'information'): return (redirect('/'))
    # data_received = request.json
    session['name'] = request.form['name']
    session['phone'] = request.form['phone']

    if valid_sand():
        session['page'] = "time"
        return redirect("/Time")
    else:
        return redirect("/information")
