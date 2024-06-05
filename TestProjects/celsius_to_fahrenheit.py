# # Official Documentation 
# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()



# Function implementation
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Importing necessary libraries (Unit tests)
import unittest

# Unit test class for the celsius_to_fahrenheit function.
class TestCelsiusToFahrenheit(unittest.TestCase):
    
    def test_zero(self):
        # Test that 0 degrees Celsius is converted to 32 degrees Fahrenheit.
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        
    def test_boiling_water(self):
        # Test that 100 degrees Celsius is converted to 212 degrees Fahrenheit.
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        
    def test_negative(self):
        # Test that -40 degrees Celsius is converted to -40 degrees Fahrenheit.
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)
        
    def test_decimals(self):
        # Test the conversion of a decimal value and check precision up to 3 decimal places.
        self.assertAlmostEqual(celsius_to_fahrenheit(37.78), 100.004, places=3)
        
    def test_integer_type(self):
        # Test that the function returns a float type for integer inputs.
        self.assertIsInstance(celsius_to_fahrenheit(0), float)

    def test_freezing_point(self):
        # Test that the freezing point of water (0 degrees Celsius) is converted correctly.
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_body_temperature(self):
        #  Test that the average human body temperature (37 degrees Celsius) is converted correctly.
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

    def test_high_temperature(self):
        # Test the conversion of a high temperature value (e.g., 1000 degrees Celsius).
        self.assertEqual(celsius_to_fahrenheit(1000), 1832.0)

if __name__ == '__main__':
    unittest.main()