class TennisGame:

    def __init__(self):
        self.player1_points = 0
        self.player2_points = 0

    def score_point(self, is_player1_scored):
        if is_player1_scored:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        return "Love-All"