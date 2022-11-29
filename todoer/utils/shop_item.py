from .db_handler import Points

class ShopItem:
    def __init__(self, name, price, effect, description):
        self.name = name
        self.price = price
        self.effect = effect
        self.description = description

items = {'Mana Potion':[20, 'add_10_Mana', 'Mana +10'], 'Summoning Sticker':[1000, 'Summoning_sticker_added_to_inventory', 'Summon a Familiar']}

async def getShop():
    item_objs = []
    for i in items:
        # print(i)
        to_obj = ShopItem(i, items[i][0], items[i][1], items[i][2])
        # print(to_obj)
        item_objs.append(to_obj)
    return item_objs

async def buy_item(data, user_id):
    alert_text = ''
    item_price = int(data[2])
    operation = data[3] 
    effected_by = data[4]

    # print(f"{operation} {effected_by} to {effected_value}\n")
    alert_text+=f"{Points.sub(user_id, 'Coins', item_price)}\n"
    if operation == 'add':
        alert_text+=Points.add(user_id, 'Mana', int(effected_by))
    else:
        alert_text+=f"\nSummoning Sticker added to inventory"
    return alert_text
