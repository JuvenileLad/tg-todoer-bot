from ..client import myColl
import random

def  user_inDB(user_id):
    if myColl.find_one({"_id": user_id}):
        return myColl.find_one({"_id": user_id})
    return False

def  task_inDB(user_id, task_id):
    a = myColl.find_one({"_id": user_id})
    if int(task_id) in a['tasks']:
        return True
    return False

def get_tasksList(user_id):
    a = myColl.find_one({"_id":user_id})
    try:
        list = a['tasks']
        return list
    except:
         return False
    
def get_leaderboard():
    unordered = {}
    leaderboard = {}
    for i in myColl.find():
        unordered[i['_id']] = i['Coins']
    for key in sorted(unordered.values(), reverse=True):
        # list(unordered.values()) - convert to list

        # ..index(key) - to get the index value at which key
        # i.e. USER_ID falls

        # list(unordered.keys())[..] - to get the value which falls
        # at index from list of keys in unordered

        # https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
        leaderboard[list(unordered.keys())[list(unordered.values()).index(key)]] = key
        unordered.pop(list(unordered.keys())[list(unordered.values()).index(key)])
    return leaderboard

class Points:
    def HealthBar(HP):
        full, empty = '▰', '▱'
        total = (full * HP)+((10-HP)*empty)
        return total
        
    def checkHP(user_id):
        a = myColl.find_one({"_id":user_id})
        hp = a['HP']
        return hp
    def genRandom(min, max):
        return random.randint(min, max)

    def reset(user_id):
        myColl.update_one({"_id": user_id}, {"$set": {"HP": 100, "Coins": 0}})
    
    def current(user_id, type):
        a = myColl.find_one({"_id": user_id})
        return a['HP']
    
    def add(user_id, type, amount):
        a = myColl.find_one({"_id": user_id})
        myColl.update_one({"_id": user_id}, {"$inc": {type: amount}})
        return f"{type} +{amount}"
    
    def sub(user_id, type, amount):
        a = myColl.find_one({"_id": user_id})
        myColl.update_one({"_id": user_id}, {"$inc": {type: -amount}})
        return f"{type} -{amount}"

class Task:
    def __init__(self, user_id, task_id):
        self.userID = user_id
        self.taskID = task_id
        self.user = user_inDB(user_id) 
        self.task = task_inDB(user_id, task_id) if self.user else False
        # print(f"User: {self.user}, Task: {self.task}")

    def add_task(self):
        if not self.user:
            myColl.insert_one({"_id": self.userID, "tasks": [self.taskID], "HP": 100, "Coins": 0})
        if self.user and not self.task:
            myColl.update_one({"_id": self.userID}, {"$push": {"tasks": self.taskID}})

    def remove_task(self, type):
        if self.user and self.task:
            hp = Points.checkHP(self.userID)
            if hp<=0:
                Points.reset(self.userID)
                return "HP & Coins reset!"
            if type == 'done':
                amount = Points.genRandom(1, 5)
                text = Points.add(self.userID, 'Coins', amount)
            elif type == 'missed':
                amount = Points.genRandom(10, 20)
                text = Points.sub(self.userID, 'HP', amount)
            elif type == 'postponed':
                amount = Points.genRandom(1, 3)
                text = Points.sub(self.userID, 'Coins', amount)
            myColl.update_one({"_id": self.userID}, {"$pull": {"tasks": int(self.taskID)}})
            return text
