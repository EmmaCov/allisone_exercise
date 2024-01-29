import unittest
import numpy as np

import ML_Coding_exercise.src.main as main
from ML_Coding_exercise.src.domain.preprocess import preprocess

model = main.DiamondModel()

class APITestCase(unittest.TestCase):

    def test_score(self):
        result = model.score()
        self.assertTrue(result>=0.97)

    def test_preprocess(self):
        data = [1.01, "Ideal", "G", "VS2", "VG", "EX", "GIA"]
        processed_data = preprocess(data)
        expected_output = np.array([1.01, 2.00, 3.00, 4.00, 3.00, 0.00, 1.00])
        
        self.assertEqual(len(processed_data), len(expected_output))
        for i in range(len(processed_data)):
            self.assertEqual(processed_data[i], expected_output[i])

if __name__ == '__main__':
    unittest.main()
