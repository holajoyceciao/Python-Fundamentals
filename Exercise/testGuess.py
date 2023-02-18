import unittest
import guessGame

class TestGame(unittest.TestCase):
    def test_game(self):
        result = guessGame.game(5, 5)
        self.assertTrue(result)

    def test_game_wrong_guess(self):
        result = guessGame.game(5, 6)
        self.assertFalse(result)

    def test_game_wrong_number(self):
        result = guessGame.game(5, 11)
        self.assertFalse(result)

    def test_game_wrong_type(self):
        result = guessGame.game(5, '5')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()