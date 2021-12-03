from pymongo import MongoClient

class Database:
    def __init__(self, tabel_name):
        self.client = MongoClient()
        self.db = self.client.Dotmac
        self.collection = self.db[tabel_name]
    
    def insert(self, data):
        self.collection.insert_one(data)
    
    def find(self, data):
        return self.collection.find(data)

    def find_one(self, data):
        return self.collection.find_one(data)
    
    def update(self, id, data):
        self.collection.update_one(id, data)

    def delete(self, data):
        self.collection.delete_one(data)
    
    def delete_many(self, data):
        self.collection.delete_many(data)
    