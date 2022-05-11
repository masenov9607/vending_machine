from controller import *
from unittest import TestCase
from models import *

class VendingMachineControllerTest(TestCase):
    def create_products(self):
        self.products = Inventory()._products
        self.products[46] = Product("PEPSI",70,46)
        self.products[37] = Product("7Days",60,37)
        self.products[23] = Product("Mineral water",10,23)
        VendingMachineCoins().add_coins(10,15)
        VendingMachineCoins().add_coins(20,5)
        VendingMachineCoins().add_coins(50,10)
        VendingMachineCoins().add_coins(100,7)

    def test_push_product(self):
        self.create_products()
        VendingMachineController().push_product(46,5)
        VendingMachineController().push_product(37,10)
        VendingMachineController().push_product(23,7)
        self.assertTrue(Inventory().get_product_quantity(46) == 5)
        self.assertTrue(Inventory().get_product_quantity(37) == 10)
        self.assertTrue(Inventory().get_product_quantity(23) == 7)

    def test_calculate_change(self):
        self.create_products()
        order1 = Order(46,80)
        order2 = Order(46,81)
        changed_coins = VendingMachineController().calculate_change(order1)
        self.assertTrue(changed_coins == [10])

        changed_coins = VendingMachineController().calculate_change(order2)
        self.assertTrue(changed_coins == [])

    def test_get_product(self):
        VendingMachineController().push_product(46,5)
        VendingMachineController().push_product(37,10)
        order1 = Order(46,80)
        expected = f"Take your product PEPSI"
        actual = VendingMachineController().get_product(order1)
        self.assertTrue(actual ==  expected)
        self.assertTrue(VendingMachineCoins().coins[Coins(10)] == 14)
        self.assertTrue(Inventory().get_product_quantity(46) == 4)

        order2 = Order(46,50)
        expected = "You need to enter extra 20"
        actual = VendingMachineController().get_product(order2)
        self.assertTrue(actual ==  expected)
        self.assertTrue(VendingMachineCoins().coins[Coins(10)] == 14)
        self.assertTrue(Inventory().get_product_quantity(46) == 4)

        order3 = Order(46,81)
        expected = f"Not enough money to return"
        actual = VendingMachineController().get_product(order3)
        self.assertTrue(actual ==  expected)
        self.assertTrue(VendingMachineCoins().coins[Coins(10)] == 14)
        self.assertTrue(Inventory().get_product_quantity(46) == 4)

        order3 = Order(23,81)
        expected = f"No such product Mineral water"
        actual = VendingMachineController().get_product(order3)
        self.assertTrue(actual ==  expected)







    
