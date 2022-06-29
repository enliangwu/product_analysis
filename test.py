import unittest
from product_analysis import get_products
'''
@author Enliang Wu

A test file for product_analysis.py
'''


class TestProductSolution(unittest.TestCase):
    def test_product_filter(self):
        # all product must not be hidden and deleted
        for product in get_products():
            self.assertFalse(product["deleted"])
            self.assertFalse(product["hidden"])

    def test_product_duplicate(self):
        # there should not be any duplicated products
        product_ids = set()
        for product in get_products():
            self.assertFalse(product["id"] in product_ids)
            product_ids.add(product["id"])

    def test_product_order(self):
        # the product must be ordered by price and name
        last_product = None
        for product in get_products():
            if last_product is None:
                last_product = product
                continue

            # the last product' price must less or equal than current one
            self.assertTrue(float(last_product["price"].replace("$", "")) <= float(product["price"].replace("$", "")))

            if float(last_product["price"].replace("$", "")) == float(product["price"].replace("$", "")):
                # if last product has the same name with current one, its name needs to come before the current product
                self.assertTrue(last_product["product_name"] < product["product_name"])


if __name__ == '__main__':
    unittest.main()
