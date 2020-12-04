from controller import Controller
from view import View
from vote import Vote
from mission_decision import MissionDecision
from typing import List

class CliController(Controller):
    def __init__(self, view: View):
        super().__init__(view)

    def get_vote(self, team: List[int]):
        vote_map = {"a": Vote.ACCEPT, "r": Vote.REJECT}
        display_message = ("Vote 'A' for accept or 'R' for" +
            " reject on the team with players: " + ''.join(map(str, team)))
        vote = input(display_message).lower()
        while vote not in vote_map:
            vote = input("Vote was not one of 'A' or 'R', try again.").lower()
        return vote_map[vote]

    def get_mission_decision(self):
        decision_map = {"s": MissionDecision.SUCCESS, "f": MissionDecision.FAIL}
        display_message = "Vote 'S' for success or 'F' for failure"
        decision = input(display_message).lower()
        while decision not in decision_map:
            decision = input("Decision was not one of 'S' or 'F', try again.")
        return decision_map[decision]

    def get_team(self, num_members: int, total_players: int):
        display_message = ("Please choose {} space-separated players for the mission."
                            .format(num_members))
        team = self._team_from_input(input(display_message))
        while self._is_not_valid_team(team, num_members, total_players):
            team = self._team_from_input(input("Try again."))
        return team

    def _team_from_input(self, inp: str):
        return list(map(int, inp.split()))

    def _is_not_valid_team(self, 
            team: List[int], 
            num_members: int, 
            total_players: int):
        return (len(team) != num_members or 
                len(set(team)) != len(team) or
                any(member not in range(total_players) for member in team))