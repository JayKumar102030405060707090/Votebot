class Database:
    def __init__(self):
        self.votes = {}

    def add_vote(self, user_id, poll_id):
        if poll_id not in self.votes:
            self.votes[poll_id] = set()
        self.votes[poll_id].add(user_id)

    def remove_vote(self, user_id, poll_id):
        if poll_id in self.votes and user_id in self.votes[poll_id]:
            self.votes[poll_id].remove(user_id)

    def get_votes(self, poll_id):
        return len(self.votes.get(poll_id, set()))
