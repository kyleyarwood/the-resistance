from character import Character
from mission_decision import MissionDecision
from vote import Vote
from typing import List
from game import Game
from controller import Controller

class Resistance(Character):
    def __init__(self, game: Game, cpu: bool, controller: Controller):
        super().__init__(game, cpu, controller)

    def mission_decision(self):
        return MissionDecision.SUCCESS

    def _cpu_vote(self, team: List[int]):
        #TODO: figure out a strategy for the computer voting
        return Vote.ACCEPT

    def _cpu_choose_team(self, num_members: int):
        #TODO: figure out how the computer should choose their team
        return list(range(num_members))
