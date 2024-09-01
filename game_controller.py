from game import Game, GameStatistics

class GameController:
    def __init__(self, game: Game, statistics: GameStatistics):
        self.game = game
        self.statistics = statistics
    
    def play(self):
        print(self.game.start())
        while True:
            try:
                user_guess = int(input("Tebak Angkanya Sob!: "))
                result = self.game.guess(user_guess)
                print(result)
                if result.startswith("Keren Sob!"):
                    break
                print(f"Percobaan: {self.statistics.get_attempts()}")
            except ValueError:
                print("Harus Masukin Angka Sob!.")
    
    def show_stats(self):
        print(f"Total Percobaan: {self.statistics.get_attempts()}")
        print(f"Hasil Akhir: {self.statistics.get_last_result()}")

#_________________#
#Alman Kamal Mahdi#
# 211201221200244 #
#_________________#
