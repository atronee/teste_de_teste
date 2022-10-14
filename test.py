import pizza
import unittest
from mock import patch

@patch('pizza.ingredientes', {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {'gorgonzola': 2}})


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

    @patch('pizza.ingredientes', {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {'gorgonzola': 2}})
    def test_case_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(pizza.cadastrar_ingrediente("massa", "trigo1", 19.342), {'massa': {'trigo': 19.34, 'trigo1': 19.342}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {'gorgonzola': 2}})
    
    @patch('pizza.ingredientes', {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {'gorgonzola': 2}})
    def test_case_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(pizza.listar_ingredientes("massa"), {'trigo': 19.34})

    @patch('pizza.ingredientes', {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {'gorgonzola': 2}})
    def test_case_floats_positive_positive(self):
        print('\nExecuting Case Test: Floats - Positive - Positive')
        self.assertAlmostEqual(pizza.montar_pizzza_valor("trigo", "tomate", "gorgonzola", "pepperoni"), 31.34)

    @patch('pizza.ingredientes', {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {'gorgonzola': 2}})
    def test_case_floats_negative_negative(self):
        print('\nExecuting Case Test: Floats - Negative - Negative')
        self.assertAlmostEqual(pizza.remover_ingrediente("cobertura", "pepperoni"), {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {}, 'queijo': {'gorgonzola': 2}})


if __name__ == '__main__':
    unittest.main(verbosity=2)
