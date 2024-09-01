from game import NumberGuessingGame
from game_controller import GameController

def main():
    game = NumberGuessingGame(lower_bound=1, upper_bound=100)
    controller = GameController(game=game, statistics=game)
    
    controller.play()
    controller.show_stats()

if __name__ == "__main__":
    main()

#_________________#
#Alman Kamal Mahdi#
# 211201221200244 #
#_________________#