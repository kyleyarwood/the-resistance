from character import Character
from mission_decision import MissionDecision
from vote import Vote

class Resistance(Character):
    def __init__(self, game: Game, cpu: bool, controller: Controller):
        super().__init__(game, cpu, controller)

    def mission_decision(self):
        return MissionDecision.SUCCESS

    def _cpu_vote(self, team: List[int]):
        return Vote.ACCEPT

    def _cpu_choose_team(self, num_members: int):
        return list(range(num_members))
