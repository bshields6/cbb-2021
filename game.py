class Game:
    """One game."""
    def __init__(self, MOV, oppName, oppRating, home, day):
        """Initialize the game."""
        self.MOV = MOV
        self.day = day
        self.isWon = MOV > 0
        self.home = home
        self.oppName = oppName
        self.oppRating = oppRating
        self.rating = self.calculateGameRating()

    def calculateGameRating():
        """Calculate rating for protagonist team."""
        oppR = self.oppRating
        if oppR >= 0:
            ratingCoef = sqrt(oppR)
            if oppR > GOOD_TEAM_CUTOFF:
                ratingCoef += GOOD_TEAM_BOOST

        else:
            ratingCoef = -sqrt(abs(oppR))

        if self.isWon:
            rating = (ratingCoef * OPP_RATING_WEIGHT) + WIN_BOOST + sqrt(self.MOV)
        else:
            rating = (ratingCoef * OPP_RATING_WEIGHT) - WIN_BOOST - sqrt(abs(self.MOV))

        if self.day > ROAD_GAME_START:
            if self.home:
                rating -= ROAD_BOOST
            else:
                rating += ROAD_BOOST

        dayCoef = sqrt((self.day / 1000) + 1)
        rating *= dayCoef
        return rating