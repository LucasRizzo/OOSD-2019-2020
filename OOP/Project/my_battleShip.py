import random
import os
from playsound import playsound


class Board:
    def __init__(self, width=10, length=10):
        self.width = 10
        self.length = 10
        self.selfCoordinates = ["-"] * self.length
        for i in range(self.length):
            self.selfCoordinates[i] = ["-"] * self.width

        self.targetCoordinates = ["-"] * self.length
        for i in range(self.length):
            self.targetCoordinates[i] = ["-"] * self.width

    def __str__(self):

        # Print top coordinates
        board = " " * 40 + "Own board" + " " * 31 + " Target board \n"
        # Top coordinates self
        board = "\t"
        for x in range(self.width):
            board += str(x + 1) + "\t"
        board += " | "
        # Top coordinates target
        board += "   \t"
        for x in range(self.width):
            board += str(x + 1) + "\t"
        board += " | \n"

        # Print rows
        for x in range(self.width):
            # Coordinate of the row
            board += str(x + 1) + "\t"
            for y in range(self.length):

                if self.selfCoordinates[x][y] != "*":
                    board += self.selfCoordinates[x][y] + "\t"
                else:
                    board += "\033[1;32;40m" + self.selfCoordinates[x][y] + "\t\033[1;30;37m"
            board += " | "
            # Coordinate of the row
            board += str(x + 1) + "\t"
            for y in range(self.length):
                if self.targetCoordinates[x][y] != "*":
                    board += self.targetCoordinates[x][y] + "\t"
                else:
                    board += "\033[3;31;40m" + self.targetCoordinates[x][y] + "\t\033[1;30;37m"
            # Break line
            board += " | \n"
        return board

    def setShips(self, ships: dict):
        for ship, size in ships.items():
            if ship == "A":
                for i in range(size):
                    self.selfCoordinates[0][i] = ship
            if ship == "B":
                for i in range(size):
                    self.selfCoordinates[3][i] = ship
            if ship == "S":
                for i in range(size):
                    self.selfCoordinates[i][9] = ship
            if ship == "D":
                for i in range(size):
                    self.selfCoordinates[i][8] = ship
            if ship == "P":
                for i in range(size):
                    self.selfCoordinates[i][7] = ship


class Player(Board):
    def __init__(self, name: str):
        Board.__init__(self)
        self.ships = {"A": 5,  # "Aircraft Carrier"
                      "B": 4,  # "Battleship"
                      "S": 3,  # "Submarine"
                      "D": 3,  # "Destroyer"
                      "P": 2}  # "Patrol Boat"
        self.setShips(self.ships)
        self.score = 0
        self.name = name
        self.hits = 0
        self.previousHit = {"miss": "y", "x": 0, "y": 0}

    def __str__(self):
        return super(Player, self).__str__()

    def next_move(self) -> tuple:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        while self.targetCoordinates[x][y] != "-":
            x = random.randint(0, 9)
            y = random.randint(0, 9)

        self.targetCoordinates[x][y] = "*"
        return x, y


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]

    def updateBoards(self):
        clear = lambda: os.system('cls')
        clear()
        string_game = ""

        string_game += " -" + "-" * 80 + "    " + self.players[0].name + " board (" + str(
            self.players[0].hits) + ")    " + "-" * 74 + "\n"
        string_game += self.players[0].__str__()
        string_game += " " + "-" * 177 + "\n"
        string_game += " -" + "-" * 80 + "    " + self.players[1].name + " board (" + str(
            self.players[1].hits) + ")    " + "-" * 74 + "\n"
        string_game += self.players[1].__str__()
        string_game += " --------------------- \n"
        print(string_game)

    def play(self):
        who_plays = random.randint(0, 1)
        target = abs(who_plays - 1)

        print("Welcome to the automated battle ship!")
        print("Two players are duelling today!")
        print(".")
        print(".")
        print(".")
        print(self.players[who_plays].name, "VS", self.players[target].name)
        print(".")
        print(".")
        print(".")
        print("May the best win!")
        input("Press enter to continue...")

        while True:
            x, y = self.players[who_plays].next_move()

            hit = self.players[target].selfCoordinates[x][y] != "-"

            if hit:
                self.players[who_plays].hits += 1
                self.players[target].selfCoordinates[x][y] = "*"

            self.updateBoards()

            if hit:
                hit_message = self.players[who_plays].name + " hit a ship at (" + str(x + 1) + ", " + str(y + 1) + ")!"
                print(hit_message)
                playsound('shot.mp3')
            else:
                miss_message = self.players[who_plays].name + " shot at (" + str(x + 1) + ", " + str(
                    y + 1) + ") and missed!"
                print(miss_message)
                playsound('water.mp3')

            if self.players[who_plays].hits == 17:
                print(self.players[who_plays].name, "won! Congratulations!")
                break

            who_plays = abs(who_plays - 1)
            target = abs(target - 1)
            # input("Press enter to continue:")


player1 = Player("Lucas")
player2 = Player("Sarah")
game = Game(player1, player2)
game.play()
