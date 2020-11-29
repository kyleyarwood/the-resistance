from character import Character
from game import Game
from controller import Controller
from mission_decision import MissionDecision
from vote import Vote
from typing import List

class Spy(Character):
    def __init__(self, game: Game, cpu: bool, controller: Controller):
        super().__init__(game, cpu, controller)

    def mission_decision(self):
        if self.cpu:
            return self._cpu_mission_decision()
        player_decision = self.controller.get_decision()
        return player_decision

    def _cpu_vote(self, team: List[int]):
        return Vote.ACCEPT

    def _cpu_mission_decision(self):
        return MissionDecision.FAIL

    def _cpu_choose_team(self, num_members):
        return list(range(num_members))