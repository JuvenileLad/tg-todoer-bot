from .db_handler import Points

class ShopItem:
    def __init__(self, name, price, effect, description):
        self.name = name
        self.price = price
        self.effect = effect
        self.description = description

items = {'Mana Potion':[20, 'add_10_Mana', 'Mana +10'], 'Health Potion':[100, 'add_5_HP', 'HP +5']}

async def getShop():
    item_objs = []
    for i in items:
        to_obj = ShopItem(i, items[i][0], items[i][1], items[i][2])
        item_objs.append(to_obj)
    return item_objs

async def buy_item(data, user_id):
    alert_text = ''
    item_price = int(data[2])
    operation = data[3] 
    effected_by = data[4]

    alert_text+=f"{Points.sub(user_id, 'Coins', item_price)}\n"
    if operation == 'add':
        value_effected = data[5]
        alert_text+=Points.add(user_id, value_effected, int(effected_by))
    # TODO: add other operations
    return alert_text
