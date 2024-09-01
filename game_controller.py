from game import Game, GameStatistics

class GameController:
    def __init__(self, game: Game, statistics: GameStatistics):
        self.game = game
        self.statistics = statistics
    
    def play(self):
        print(self.game.start())
        while True:
            try:
                user_guess = int(input("Enter your guess: "))
                result = self.game.guess(user_guess)
                print(result)
                if result.startswith("Congratulations"):
                    break
                print(f"Attempts: {self.statistics.get_attempts()}")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def show_stats(self):
        print(f"Total attempts: {self.statistics.get_attempts()}")
        print(f"Last result: {self.statistics.get_last_result()}")

#_________________#
#Alman Kamal Mahdi#
# 211201221200244 #
#_________________#