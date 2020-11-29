from character import Character
from mission_decision import MissionDecision
from vote import Vote
from typing import List

class Spy(Character):
    def __init__(self, game: 'Game', controller: 'Controller'):
        super().__init__(game, controller)

    def mission_decision(self):
        if self.cpu:
            return self._cpu_mission_decision()
        player_decision = self.controller.get_decision()
        return player_decision

    def _cpu_vote(self, team: List[int]):
        #TODO: figure out a strategy for the computer voting
        return Vote.ACCEPT

    def _cpu_mission_decision(self):
        #TODO: figure out when it is best for the computer spy to choose fail
        return MissionDecision.FAIL

    def _cpu_choose_team(self, num_members):
        #TODO: figure out how the computer should choose their team
        return list(range(num_members))

    def __str__(self):
        return "Spy {}".format(self.player_num)
