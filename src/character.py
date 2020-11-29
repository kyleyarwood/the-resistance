from controller import Controller
from game import Game
from typing import List

class Character(object):
    player_num = 0
    def __init__(self, game: Game, cpu: bool, controller: Controller):
        self.game = game
        self.cpu = cpu
        self.controller = controller
        self.player_num = Character.player_num
        Character.player_num += 1

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
