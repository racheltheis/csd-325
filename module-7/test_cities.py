#Rachel Theis
#Module 7.2
#CSD 325

#test_cities

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        result = city_country("Berlin", "Germany")
        self.assertEqual(result, "Berlin, Germany")

        result = city_country("Tokyo", "Japan")
        self.assertEqual(result, "Tokyo, Japan")

        result = city_country("Los Angeles", "USA")
        self.assertEqual(result, "Los Angeles, USA")

        result = city_country("", "")
        self.assertEqual(result, ", ")

if __name__ == "__main__":
    unittest.main()