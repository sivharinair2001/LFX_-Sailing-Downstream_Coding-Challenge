import unittest

def process_list(input_list):
    # Check if the length of the input list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("The length of the list must be a multiple of 10.")

    # Remove items at positions which are a multiple of 2 or 3
    result_list = [num for i, num in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

    return result_list

class TestProcessList(unittest.TestCase):
    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = process_list(input_list)
        self.assertEqual(result, [1, 5, 7, 11, 13, 17, 19])

    def test_invalid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # Not a multiple of 10
        with self.assertRaises(ValueError):
            process_list(input_list)

if __name__ == '__main__':
    unittest.main()



