from controller import Controller
from game import Game

class Character(object):
    player_num = 0
    def __init__(self, game: Game, cpu: bool, controller: Controller):
        self.game = game
        self.cpu = cpu
        self.controller = controller
        self.player_num = player_num
        player_num += 1

    def vote(self, team: List[Character]):
        pass
    
    def mission_decision(self):
        pass

    def choose_team(self, num_members: int):
        pass