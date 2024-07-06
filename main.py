import os
import sys
import json
import time
import random

from itertools import cycle
from colorama import Fore, init

rounds = 5

class DiceProject:
    def __init__(self):
        self.auth = json.loads(open("authdb.json", "r").read())

        self.playerOnePoints = 0
        self.playerTwoPoints = 0

        self.diceArt = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
        }

    """Print dice art"""
    """def printArt(self):
        for line in self.diceArt[1]:
            print(line)"""

    def AnimationManager(self, duration, diceRolled, player):
        animation = "|/-\\"
        startTime = time.time()
        while True:
            for i in range(4):
                time.sleep(0.1)
                sys.stdout.write("\r" + f"{Fore.GREEN}Rolling dice... " + f"{Fore.GREEN}[{animation[i % len(animation)]}]")
                sys.stdout.flush()
            if time.time() - startTime > duration:
                break

        sys.stdout.write("\r" + f"\r\n{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Player{player} rolled a {diceRolled}\n")

        for i in self.diceArt[diceRolled]:
            print(Fore.GREEN + i)

        return diceRolled




    def start(self):

        input(f"\n{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}]{Fore.GREEN} Welcome, any key to start! \n")

        player1 = 0
        player2 = 0

        for i in range(rounds):

            print(Fore.GREEN + "─────────────────────────────────────────────────────────────────────────────────")
            for i in range(2):
                player1 += self.AnimationManager(2, random.randint(1, 6), 1)
                player2 += self.AnimationManager(2, random.randint(1, 6), 2)

            print(" ")
            if player1 % 2 == 0:
                print(f"{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Player 1 scored an even total, therefore, they've gained 10 points!")
                self.playerOnePoints += 10
            else:
                print(f"{Fore.WHITE}[{Fore.RED}ⅹ{Fore.WHITE}]{Fore.RED} Player 1 scored an odd total, therefore, they've lost 5 points!")
                self.playerOnePoints -= 5
                if self.playerOnePoints < 0:
                    self.playerOnePoints = 0

            if player2 % 2 == 0:
                print(f"{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Player 2 scored an even total, therefore, they've gained 10 points!")
                self.playerTwoPoints += 10

            else:
                print(f"{Fore.WHITE}[{Fore.RED}ⅹ{Fore.WHITE}]{Fore.RED} Player 2 scored an odd total, therefore, they've lost 5 points!")
                self.playerTwoPoints -= 5
                if self.playerTwoPoints < 0:
                    self.playerTwoPoints = 0

        print(Fore.GREEN + "─────────────────────────────────────────────────────────────────────────────────")

        print(" ")

        if self.playerOnePoints == self.playerTwoPoints:
            print(f"{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Both players drew with {self.playerOnePoints} points!")
            return

        if self.playerOnePoints > self.playerTwoPoints:
            print(f"{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Player 1 won with {self.playerOnePoints} points!")
            print(f"{Fore.WHITE}[{Fore.RED}ⅹ{Fore.WHITE}]{Fore.RED} Player 2 lost with {self.playerTwoPoints} points!")
        else:
            print(f"{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Player 2 won with {self.playerTwoPoints} points!")
            print(f"{Fore.WHITE}[{Fore.RED}ⅹ{Fore.WHITE}]{Fore.RED} Player 1 lost with {self.playerOnePoints} points!")



    def main(self):
        auth1 = input(f"{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Enter player1's password >> ")
        auth2 = input(f"{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}]{Fore.GREEN} Enter player2's password >> ")

        print(" ")

        if auth1 == self.auth['player1'] and auth2 == self.auth['player2']:
            self.start()
        else:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED} Invalid credentials! ")


if __name__ == '__main__':

    init(autoreset=True)

    DiceProject().main()