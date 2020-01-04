import unittest
# import testing_in_python.exercise_testing.exerciseTesting_file
import exerciseTesting_file

class TestGame(unittest.TestCase):
    def test_input(self):
        # answer = 5
        # guess = 5
        # result = exerciseTesting_file.run_guess(guess, answer)
        result = exerciseTesting_file.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = exerciseTesting_file.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = exerciseTesting_file.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = exerciseTesting_file.run_guess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()



