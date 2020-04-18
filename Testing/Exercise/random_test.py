import unittest
import guess


class TestGuess(unittest.TestCase):
    def test_guess_true(self):
        result = guess.run_guess(5, 5)
        self.assertTrue(result)

    def test_guess_false_err1(self):
        result = guess.run_guess(0, 5)
        self.assertFalse(result)

    def test_guess_false_err2(self):
        result = guess.run_guess(11, 5)
        self.assertFalse(result)

    def test_guess_string_err(self):
        result = guess.run_guess('string', 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
