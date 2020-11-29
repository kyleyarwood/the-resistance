from random import shuffle, randrange
from typing import List, Type
from spy import Spy
from resistance import Resistance
from vote import Vote
from mission_decision import MissionDecision

class Game(object):
    MIN_PLAYERS = 5
    MAX_PLAYERS = 10
    NUM_ROUNDS = 5
    MAX_FAILS = 4
    def __init__(self, num_players: int, num_cpu: int, controller: 'Controller'):
        assert Game.MIN_PLAYERS <= num_players <= Game.MAX_PLAYERS, """
                    The number of players should be in the range [{},{}]""".format(
                    Game.MIN_PLAYERS,
                    Game.MAX_PLAYERS
                )
        self.num_players = num_players
        self.num_cpu = num_cpu
        self.controller = controller
        self.resistance_counter = 0
        self.spy_counter = 0
        self.vote_fail_counter = 0
        self.players = []
        self.num_players_on_mission = self._get_num_players_on_mission()

    def _get_num_players_on_mission(self):
        if self.num_players >= 8:
            return [3,3,4,4,5]
        num_players_on_mission = [2,3,
                (self.num_players-1)//2,(self.num_players+1)//2,3]
        if self.num_players == 6:
            num_players_on_mission[2] = 4
        return num_players_on_mission

    def play_game(self):
        mission_leader = randrange(self.num_players)
        while not self._is_game_over():
            if self.vote_fail_counter == Game.MAX_FAILS:
                self.mission_fail()
                continue
            mission_team = self.players[mission_leader].choose_team(
                self.num_players_on_mission[self.mission_no()])
            team_votes = self.receive_team_votes(mission_team)
            if self.is_team_rejected(team_votes):
                self.vote_fail_counter += 1
                mission_leader = (mission_leader+1)%self.num_players
                continue
            is_mission_passed = self.receive_mission_decision(
                list(map(lambda x: self.players[x], mission_team)))
            if is_mission_passed:
                self.mission_success()
            else:
                self.mission_fail()
            mission_leader = (mission_leader+1)%self.num_players
        return self.spy_counter > self.NUM_ROUNDS//2

    def is_team_rejected(self, team_votes: List[Vote]):
        return sum(vote == Vote.REJECT 
                for vote in team_votes) >= self.num_players//2

    def mission_fail(self):
        self.spy_counter += 1

    def mission_success(self):
        self.resistance_counter += 1

    def receive_team_votes(self, mission_team: List['Character']):
        return [player.vote(mission_team) for player in self.players]

    def receive_mission_decision(self, mission_team: List['Character']):
        threshold = 1 if self.num_players >= 7 and self.mission_no() == 3 else 0
        return sum(player.mission_decision() == MissionDecision.FAIL
                    for player in mission_team) <= threshold

    def mission_no(self):
        return self.spy_counter + self.resistance_counter

    def receive_chosen_team(self, player: 'Character'):
        return player.choose_team()

    def _assign_roles(
        self, 
        num_regular_spies: int, 
        num_regular_resistance: int,
        special_roles: List[Type] = []):
        players = [Spy(self, self.controller) 
                        for _ in range(num_regular_spies)]
        players += [Resistance(self, self.controller)
                        for _ in range(num_regular_resistance)]
        players += [role(self, self.controller) 
                            for role in special_roles]
        shuffle(players)
        for i, player in enumerate(players):
            if i < self.num_cpu:
                player.cpu = True
            player.player_num = i
        return players

    def _is_game_over(self):
        return (self.resistance_counter > Game.NUM_ROUNDS//2 or 
                self.spy_counter > Game.NUM_ROUNDS//2)
