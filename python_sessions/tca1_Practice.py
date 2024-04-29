import random


class IPL:
    def __init__(self, teams, trophies):
        self.teams = teams
        self.trophies = trophies

    def change_trophies(self, new_trophies):
        self.trophies = new_trophies


Mumbai = IPL('MI', 5)
print("Team:", Mumbai.teams)
Bangalore = IPL('RCB', 0)
print("RCB trophies before 2024:",Bangalore.trophies)
Bangalore.change_trophies(1)
print("RCB trophies after 2024:", Bangalore.trophies)
