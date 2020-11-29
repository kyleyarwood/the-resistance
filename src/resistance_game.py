from game import Game

class ResistanceGame(Game):
    def __init__(self, num_players: int, num_cpu: int, controller: 'Controller'):
        super().__init__(num_players, num_cpu, controller)
        num_spies = self._get_num_spies(num_players)
        self.players = self._assign_roles(
            num_spies,
            num_players - num_spies)

    def _get_num_spies(self, num_players):
        return (num_players + 2)//3
