import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_zero(self):
        self.assertEqual(self.calc.add(0,5),5)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(9,1),8)

    def test_sub_neg(self):
        self.assertEqual(self.calc.subtract(-2,-6),4)
    
    def test_mul(self):
        self.assertEqual(self.calc.multiply(4,4),16)

    def test_mul_neg(self):
        self.assertEqual(self.calc.multiply(-8,7),-56)

    def test_div_MeSes(self):
        self.assertEqual(self.calc.divide(100,21),4)
    
    def test_div_neg(self):
        self.assertEqual(self.calc.divide(-8,2),-4)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(90,30),0)
    
    def test_mod_zero(self):
        self.assertEqual(self.calc.modulo(10,0),"Division by zero")
        
if __name__ == '__main__':
    unittest.main()