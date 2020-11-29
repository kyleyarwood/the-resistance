from typing import List

class Character(object):
    def __init__(self, game: 'Game', controller: 'Controller'):
        self.cpu = False
        self.player_num = None
        self._game = game
        self._controller = controller

    def vote(self, team: List[int]):
        if self.cpu:
            return self._cpu_vote(team)
        player_vote = self.controller.get_vote(team)
        return player_vote
    
    def mission_decision(self):
        pass

    def choose_team(self, num_members: int):
        if self.cpu:
            return self._cpu_choose_team(num_members)
        player_team = self.controller.get_team(num_members)
        return player_team

    def _cpu_vote(self, team: List[int]):
        pass

    def _cpu_choose_team(self, num_members):
        pass
