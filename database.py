from pymongo import MongoClient

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["VoteBotDB"]
        self.votes = self.db["votes"]

    def add_vote(self, user_id, poll_id):
        self.votes.update_one({"poll_id": poll_id, "user_id": user_id}, {"$set": {"vote": 1}}, upsert=True)

    def remove_vote(self, user_id, poll_id):
        self.votes.delete_one({"poll_id": poll_id, "user_id": user_id})

    def get_votes(self, poll_id):
        return self.votes.count_documents({"poll_id": poll_id})
