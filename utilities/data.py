from pymongo import MongoClient
from pymongo.server_api import ServerApi

toppings = {}
toppings["Onion"] = {'id': "Onion", 'img': "/static/media/photo/topping/Onion.gif", 'double': False,
                     'description': "topping description 1", 'price': 2, 'order': 4.3}
toppings["tomato"] = {'id': "tomato", 'img': "/static/media/photo/topping/tomato.gif", 'double': False,
                      'description': "topping description 2", 'price': 2, 'order': 4}
toppings["lettuce"] = {'id': "lettuce", 'img': "/static/media/photo/topping/lettuce.gif", 'double': False,
                       'description': "topping description 3", 'price': 2, 'order': 4.1}
toppings["Beacon"] = {'id': "Beacon", 'img': "/static/media/photo/topping/Beacon.gif", 'double': False,
                      'description': "topping description 4", 'price': 12, 'order': 3}
toppings["cheese"] = {'id': "cheese", 'img': "/static/media/photo/topping/cheese.png", 'double': False,
                      'description': "topping description 5", 'price': 8, 'order': 2}
toppings["patty"] = {'id': "patty", 'img': "/static/media/photo/topping/patty.gif", 'double': False,
                     'description': "topping description 6", 'price': 25, 'order': 1}
toppings["Pickle"] = {'id': "Pickle", 'img': "/static/media/photo/topping/Pickle.png", 'double': False,
                      'description': "topping description 7", 'price': 2, 'order': 4.2}

defaultTopping = ["patty", "lettuce", "tomato", "Onion"]

products = {}

products["hamburger"] = {
    'id': "hamburger", 'price': 65,
    'description': "product description1",
    'img': "/static/media/photo/hamburger.png"}
products["drinks"] = {
    'id': "drinks",
    'price': "",
    'description': "product description2",
    'img': "/static/media/photo/drinks.png"}

products["חלשניצל"] = {
    'id': "חלשניצל",
    'price': 60,
    'description': "חלה טריה עם שניצל קריספי ורוטב הבית עם שלל ירקות",
    'img': "/static/media/photo/רון פרוייקט חלשניצל.jpg"}

products["קרם ברולה"] = {
    'id': "קרם ברולה",
    'price': 40,
    'description': "קרם ברולה אמיתי כמו באיטליה , בטוויסט שלנו, גרידת לימון בקראסט",
    'img': "/static/media/photo/קרם ברולה.jpg"}

products["ציפס-אפוי-קריספי"] = {
    'id': "ציפס-אפוי-קריספי",
    'price': 26,
    'description': "ציפס בסגנון הולנדי מוגש עם שלל מטבלים",
    'img': "/static/media/photo/ציפס-אפוי-קריספי.jpg"}

products["נקניקיה"] = {
    'id': "נקניקיה",
    'price': 35,
    'description': "נקניקית עגל איכותית נעשית במקום בתוספת ירקות ורוטב הבית",
    'img': "/static/media/photo/נקניקיה רון פרוייקט.jpg"}

products["כנפיים"] = {
    'id': "כנפיים",
    'price': 23,
    'description': "כנפיים פריכות חריפות מוגשות לצד רטבי הבית",
    'img': "/static/media/photo/כנפיים רון פרוייקט.jpg"}

products["טבעות בצל"] = {
    'id': "טבעות בצל",
    'price': 29.99,
    'description': "טבעות בצל קריספיות טריות לצד מתבלים",
    'img': "/static/media/photo/טבעות בצל רון פרוייקט.jpg"}

products["גלידה פיסטוק"] = {
    'id': "גלידה פיסטוק",
    'price': 35,
    'description': "גלידת פרווה לא טעימה לילדים מעצבנים עם רואש מוזר",
    'img': "/static/media/photo/גלידה פיסטוק.jpg"}



drinkProducts={}
drinkProducts["קולה"] = {
    'id': "קולה",
    'price': 9.99,
    'description': '330 מ"ל קולה',
    'img': "/static/media/photo/קולה.png"}


drinkProducts["קולה _דייט"] = {
    'id': "קולה _דייט",
    'price': 9.99,
    'description': '330 מ"ל קולה _דייט',
    'img': "/static/media/photo/קולה _דייט.png"}

drinkProducts["קולה _0"] = {
    'id': "קולה _0",
    'price': 9.99,
    'description': '330 מ"ל קולה _0',
    'img': "/static/media/photo/קולה _0.png"}

drinkProducts["ספרייט"] = {
    'id': "ספרייט",
    'price': 9.99,
    'description': '330 מ"ל ספרייט',
    'img': "/static/media/photo/ספרייט.png"}


drinkProducts["בירה קרה"] = {
    'id': "בירה קרה",
    'price': 80,
    'description': "1/2  בירה גולסטאר אנפילטרד",
    'img': "/static/media/photo/בירה קרה.jpg"}

drinkProducts["תה קר"] = {
    'id': "תה קר",
    'price': 15,
    'description': " תה יסמין קר ומרענן",
    'img': "/static/media/photo/תה קר רון.jpg"}

drinkProducts["לימונדה קרה"] = {
    'id': "לימונדה קרה",
    'price': 20,
    'description': "סחוט טרי בטעם של פעם",
    'img': "/static/media/photo/לימונדה קרה.jpg"}

times = {}
times['16:00'] = False
times['16:05'] = True
times['16:10'] = True
times['16:15'] = True
times['16:20'] = False
times['16:25'] = True
times['16:30'] = True
times['16:35'] = True
times['16:45'] = True
times['16:55'] = True
times['17:00'] = False
times['17:05'] = True
times['17:10'] = True
times['17:15'] = True
times['17:20'] = False
times['17:25'] = False
times['17:30'] = True
times['17:35'] = True
times['17:45'] = True
times['17:55'] = True
times['18:00'] = True
times['18:05'] = True
times['18:10'] = True
times['18:15'] = True
times['18:20'] = True
times['18:25'] = False
times['18:30'] = False
times['18:35'] = False
times['18:45'] = True
times['18:55'] = True
times['19:00'] = True
times['19:05'] = True
times['19:10'] = True
times['19:15'] = False
times['19:20'] = True
times['19:25'] = True
times['19:30'] = True
times['19:35'] = False
times['19:45'] = True
times['19:55'] = True
times['20:00'] = True
times['20:05'] = True
times['20:10'] = False
times['20:15'] = True
times['20:20'] = True
times['20:25'] = True
times['20:30'] = True
times['20:35'] = False
times['20:45'] = True
times['20:55'] = False

orders = {}
orders[0] = {
    'id ': 0,
    'products': [None],
    'price': None,
    'name': None,
    'phone': None,
    'time': None,
    'pay': None

}

################  function


######################## Data Base ###########################


uri = "mongodb+srv://user_for_web_project:password_for_web_project@cluster0.gst2cah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['db_for_web_project']
for collection in db.list_collection_names():db.drop_collection(collection)
db['toppings'].insert_many(toppings.values())
db['defaultTopping'].insert_one({"defaultTopping":defaultTopping})
db['products'].insert_many(products.values())
db['drinkProducts'].insert_many(drinkProducts.values())
db['times'].insert_many([{k: times[k]} for k in times.keys()])
db['orders'].insert_many(orders.values())

print(db)
print(db.name)
print("collection names")
print(db.list_collection_names())

