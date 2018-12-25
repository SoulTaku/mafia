#!/usr/bin/python3

class Calculator:
    def __init__(self, players, killers):
        self.players = players
        self.killers = killers

    def calculate(self, players, killers):
        if killers == 1:
            if players == 3:
                return 1/3

            elif players == 4:
                return 1/4

            return ((players - 1) * self.calculate(players-2, 1))/players + 1/players

        elif killers == 2:
            if players == 5:
                return (2/5) * (1/3)

            elif players == 6:
                return (2/6) * (1/4)

            return ((players - 2) * self.calculate(players - 2, 2))/players + (2 * self.calculate(players - 2, 1))/players

    def chance(self):
        return self.calculate(self.players, self.killers) * 100

    def unknown(self):
        return ((1 - self.calculate(self.players, 1)) * self.calculate(self.players, 2) + (1 - self.calculate(self.players, 2)) * self.calculate(self.players, 1)) * 100
