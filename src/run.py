from cli_controller import CliController
from cli_view import CliView
from resistance_game import ResistanceGame

def main():
    v = CliView()
    c = CliController(v)
    g = ResistanceGame(5, 4, c)
    print(g.play_game())

if __name__ == "__main__":
    main()
