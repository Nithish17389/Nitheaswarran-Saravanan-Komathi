import unittest
from math_quiz import generate_random_integer, choose_operator, create_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Test multiple times to check randomness
            operator = choose_operator()
            self.assertIn(operator, valid_operators)

    def test_create_problem_and_answer(self):
        
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 0, '+', '10 + 0', 10),
            (10, 0, '-', '10 - 0', 10),
            (10, 0, '*', '10 * 0', 0),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
