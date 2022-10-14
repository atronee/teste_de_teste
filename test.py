import module_quality as mq
import unittest

var_1 = 'This is a variable'

def setUpModule():
    print('\nExecuting SetUpModule')

def tearDownModule():
    print('\nExecuting TearDownModule')

class TestModuleQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nExecuting SetUpClass')

    @classmethod
    def tearDownClass(cls):
        print('\nExecuting TearDownClass')

    def setUp(self):
        print('\nExecuting SetUpMethod')

    def tearDown(self):
        print('\nExecuting TearDownMethod')
        
    def test_case_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(mq.simplest_func(1, 1), 2)

    def test_case_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(mq.simplest_func(-1, -1), -2)

    def test_case_floats_positive_positive(self):
        print('\nExecuting Case Test: Floats - Positive - Positive')
        self.assertAlmostEqual(mq.simplest_func(1.0, 1.5), 2.5, 5)

    def test_case_floats_negative_negative(self):
        print('\nExecuting Case Test: Floats - Negative - Negative')
        self.assertAlmostEqual(mq.simplest_func(-1.0, -1.5), -2.5, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
