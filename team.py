#include "Team.h"
from  globals import *
class Team:
    """The team."""
    def __init__(self, name, preRating, oStats, dStats):
        self.name = name
        self.statRating = 0
        self.seasonRating = 0
        self.preseasonRating = preRating
        self.GP = 0
        self.wins = 0
        self.losses = 0
        self.rating = 0
        self.games = []
        self.oStats = oStats
        self.dStats = dStats

    def calculateRating(self):
        """Calculate the team's rating."""
        rar = self.statRating * STAT_WEIGHT + self.seasonRating * GAME_WEIGHT  + self.preseasonRating * PRESEASON_WEIGHT
        return rar

    def addGame(self, g):
        """Add a game to the team's record."""
        self.GP += 1
        if g.isWon:
            self.wins += 1
        else:
            self.losses += 1
        self.games.append(g)
        #change seasonRating to new average of all game ratings
        total = self.seasonRating + (g.rating / self.GP)
        self.seasonRating = total / self.GP
        self.rating = self.calculateRating()

    def printGames(output):
        """Print games. In progress."""
        with open(output, 'w') as file:
            for c,g in enumerate(self.games):
                file.write(g.oppName)
                file.write(g.MOV)
