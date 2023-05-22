import pytest

from tennis import TennisGame


class TestTennisGame:

    @pytest.mark.xfail
    def test_get_score(self):
        game = TennisGame()
        assert game.get_score() == "Love-All"

        game.score_point(True)
        assert game.get_score() == "Fifteen-Love"

        game.score_point(False)
        assert game.get_score() == "Fifteen-All"

        game.score_point(True)
        assert game.get_score() == "Thirty-Fifteen"

        game.score_point(False)
        assert game.get_score() == "Thirty-All"

        game.score_point(True)
        assert game.get_score() == "Forty-Thirty"

        game.score_point(False)
        assert game.get_score() == "Deuce"

        game.score_point(True)
        assert game.get_score() == "Advantage Player 1"

        game.score_point(False)
        assert game.get_score() == "Deuce"

        game.score_point(False)
        assert game.get_score() == "Advantage Player 2"

        game.score_point(True)
        game.score_point(True)
        game.score_point(True)
        assert game.get_score() == "Win for Player 1"
