import unittest
from unittest.mock import patch
from THE_ULTIMATE_CALC import twod_operation_dialogue

class TestUltimateCalc(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_twod_operation_dialogue_perimeter(self, mock_input):
        shape = "Square"
        result = twod_operation_dialogue(shape)
        self.assertEqual(result, 1, "Should return 1 for Perimeter operation")

    @patch('builtins.input', side_effect=['2'])
    def test_twod_operation_dialogue_area(self, mock_input):
        shape = "Circle"
        result = twod_operation_dialogue(shape)
        self.assertEqual(result, 2, "Should return 2 for Area operation")

    @patch('builtins.input', side_effect=['3'])
    def test_twod_operation_dialogue_ratio(self, mock_input):
        shape = "Rectangle"
        result = twod_operation_dialogue(shape)
        self.assertEqual(result, 3, "Should return 3 for P:A ratio operation")

    @patch('builtins.input', side_effect=['4'])
    def test_twod_operation_dialogue_invalid(self, mock_input):
        shape = "Triangle"
        result = twod_operation_dialogue(shape)
        self.assertNotIn(result, [1, 2, 3], "Should not return a valid operation for invalid input")

if __name__ == '__main__':
    unittest.main()