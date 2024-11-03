import random

class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        self.choice = input(f"{self.name}, выбери камень, ножницы или бумага. Если хочешь выйти, напиши 'выход': ").lower()
        while self.choice not in ["камень", "ножницы", "бумага", "выход"]:
            print("Некорректный выбор. Пожалуйста, выбери камень, ножницы или бумага.")
            self.choice = input(f"{self.name}, выбери камень, ножницы или бумага. Если хочешь выйти, напиши 'выход': ").lower()
        return self.choice

    def random_choice(self):
        self.choice = random.choice(["камень", "ножницы", "бумага"])
        print(f"{self.name} выбрал: {self.choice}")

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def determine_winner(self):
        if self.player1.choice == self.player2.choice:
            print("Ничья!")
        elif (self.player1.choice == "камень" and self.player2.choice == "ножницы") or \
             (self.player1.choice == "ножницы" and self.player2.choice == "бумага") or \
             (self.player1.choice == "бумага" and self.player2.choice == "камень"):
            print(f"{self.player1.name} победил!")
        else:
            print(f"{self.player2.name} победил!")

    def play_round(self):
        if self.player1.choose() == "выход":
            return False
        self.player2.random_choice()
        self.determine_winner()
        return True

h_player = Player("Дима")
c_player = Player("Комп")

game = Game(h_player, c_player)

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

while True:
    if not game.play_round():
        print("Спасибо за игру! Пока!")
        break
