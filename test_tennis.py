import unittest

from tennis import Tennis

class TestTennis(unittest.TestCase):

    def setUp(self):
        self.tennis = Tennis()
    
    def test_love_all(self):
        self.assertEqual(self.tennis.score(), "love_all")

    def test_fifteen_love(self):
        self.first_score_times(1)
        self.assertEqual(self.tennis.score(), "fifteen_love")

    def test_fifteen_all(self):
        self.first_score_times(1)
        self.second_score_times(1)
        self.assertEqual(self.tennis.score(), "fifteen_all")

    def test_thirty_love(self):
        self.first_score_times(2)
        self.assertEqual(self.tennis.score(), "thirty_love")

    def test_thirty_fifteen(self):
        self.first_score_times(2)
        self.second_score_times(1)
        self.assertEqual(self.tennis.score(), "thirty_fifteen")

    def test_thirty_all(self):
        self.first_score_times(2)
        self.second_score_times(2)
        self.assertEqual(self.tennis.score(), "thirty_all")

    def test_fourty_love(self):
        self.first_score_times(3)
        self.assertEqual(self.tennis.score(), "fourty_love")

    def test_fourty_fifteen(self):
        self.first_score_times(3)
        self.second_score_times(1)
        self.assertEqual(self.tennis.score(), "fourty_fifteen")

    def test_fourty_thirty(self):
        self.first_score_times(3)
        self.second_score_times(2)
        self.assertEqual(self.tennis.score(), "fourty_thirty")

    def test_deuce(self):
        self.first_score_times(3)
        self.second_score_times(3)
        self.assertEqual(self.tennis.score(), "deuce")

    def test_first_player_advantage(self):
        self.test_deuce()
        self.first_score_times(1)
        self.assertEqual(self.tennis.score(), "first_player_advantage")

    def test_second_player_advantage(self):
        self.test_deuce()
        self.second_score_times(1)
        self.assertEqual(self.tennis.score(), "second_player_advantage")
    
    def test_first_player_win(self):
        self.test_deuce()
        self.first_score_times(2)
        self.assertEqual(self.tennis.score(), "first_player_win")

    def test_second_player_win(self):
        self.second_score_times(4)
        self.assertEqual(self.tennis.score(), "second_player_win")

    def first_score_times(self, times):
        for i in range(times):
            self.tennis.first_player_score()

    def second_score_times(self, times):
        for i in range(times):
            self.tennis.second_player_score()       


if __name__ == "__main__":
    unittest.main()