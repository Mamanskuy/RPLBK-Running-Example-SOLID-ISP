import random
from abc import ABC, abstractmethod

# Antarmuka Game
class Game(ABC):
    @abstractmethod
    def start(self):
        """Memulai permainan"""
        pass
    
    @abstractmethod
    def guess(self, number: int):
        """Membuat tebakan"""
        pass

# Antarmuka GameStatistics
class GameStatistics(ABC):
    @abstractmethod
    def get_attempts(self) -> int:
        """Mengambil jumlah tebakan"""
        pass
    
    @abstractmethod
    def get_last_result(self) -> str:
        """Mengambil hasil tebakan terakhir"""
        pass

# Implementasi NumberGuessingGame
class NumberGuessingGame(Game, GameStatistics):
    def __init__(self, lower_bound: int, upper_bound: int):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target_number = random.randint(lower_bound, upper_bound)
        self.attempts = 0
        self.last_result = ""
    
    def start(self):
        self.target_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0
        self.last_result = "Permainan Dimulai!"
        return self.last_result
    
    def guess(self, number: int):
        self.attempts += 1
        if number < self.target_number:
            self.last_result = "Angkanya KeKecilan Sob!"
        elif number > self.target_number:
            self.last_result = "Angkanya Kebesaran Sob!"
        else:
            self.last_result = "Keren Sob! Tebakanmu Benar UwU."
        return self.last_result
    
    def get_attempts(self) -> int:
        return self.attempts
    
    def get_last_result(self) -> str:
        return self.last_result

#_________________#
#Alman Kamal Mahdi#
# 211201221200244 #
#_________________#