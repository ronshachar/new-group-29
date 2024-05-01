from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user_for_web_project:password_for_web_project@cluster0.gst2cah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['db_for_web_project']


def DB_new_order():
    orders = db['orders']
    id = len(list(orders.find()))
    orders.insert_one({'id': id})
    return id


def DB_get_free_tims():
    times = db['times']
    newTims = []
    for time in list(times.find()):
        time_d = list(time.items())[1]
        if (time_d[1]):
            newTims.append(time_d[0])
    return newTims


def DB_get_products():
    return db_to_py(db['products'])


def DB_get_drinkProducts():
    return db_to_py(db['drinkProducts'])


def DB_get_toppings():
    return db_to_py(db['toppings'])


def DB_get_defaultTopping():
    return list(db['defaultTopping'].find())[0]['defaultTopping']


# change the format of the maps
def db_to_py(db_document):
    map = {}
    document = list(db_document.find())
    for item in document:
        map[item['id']] = {}
        fields = list(item.items())
        for i in range(1, len(fields)):
            map[item['id']][fields[i][0]] = fields[i][1]
    return map

# check if the time is free
def DB_is_free_time(time):
    times = db['times']
    if list(times.find({time: True})):
        return True
    return False


def DB_reels_time(time):
    times = db['times']
    times.update_one({time: False}, {'$set': {time: True}})


def DB_seize_time(time):
    times = db['times']
    times.update_one({time: True}, {'$set': {time: False}})


def DB_insert_order(order):
    orders = db['orders']
    db_order = {
        'id ': order['id'],
        'products': order['products'],
        'price': order['price'],
        'name': order['name'],
        'phone': order['phone'],
        'time': order['time'],
        'pay': order['pay']
    }
    orders.update_one({'id': order['id']}, {'$set': db_order})
