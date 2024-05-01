from flask import *

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage


from pages.homepage.subpages.home_subpages import home_subpages
app.register_blueprint(home_subpages)

from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

from pages.information.information import information
app.register_blueprint(information)

from pages.time.time import time
app.register_blueprint(time)

from pages.pay.pay import pay
app.register_blueprint(pay)

from pages.end.end import end
app.register_blueprint(end)
