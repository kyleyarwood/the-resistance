from typing import List

class Controller(object):
    def __init__(self, view: View):
        self.view = view

    def get_vote(self, team: List[int]):
        pass

    def get_decision(self):
        pass

    def get_team(self, num_members: int):
        pass