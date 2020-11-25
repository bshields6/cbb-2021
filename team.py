#include "Team.h"

class Team:
    """The team."""
    def __init__(self, name, rating):
        self.name = name
        self.statRating = 0
        self.seasonRating = 0
        self.GP = 0
        self.wins = 0
        self.losses = 0
        self.rating = rating
        self.games = []

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
        self.games.push_back(g)
        #change seasonRating to new average of all game ratings
        total = self.seasonRating + (g.rating / self.GP)
        self.seasonRating = total / self.GP
        self.rating = calculateRating()

    def printGames(output):
        """Print games. In progress."""
        with open(output, 'w') as file:
            for c,g in enumerate(games):
                file.write(g.oppName)
                file.write(g.MOV)