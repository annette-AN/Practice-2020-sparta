from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbproject

db.nextId.insert_one({'next_board': 1, 'next_category': 1, 'next_memo': 1})
