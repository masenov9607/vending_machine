from models import *
from unittest import TestCase

class InventoryTest(TestCase):

    def create_products(self):
        self.products = Inventory()._products
        self.products[46] = Product("PEPSI",70,46)
        self.products[37] = Product("7Days",60,37)
        self.products[23] = Product("Mineral water",10,23)

    def test_inventory_get_add_product(self):
        self.create_products()
        Inventory().add_product(46)
        self.assertTrue(self.products[46]._quantity == 1)

    def test_check_product_quantity(self):
        self.create_products()
        Inventory().add_product(46)
        self.assertTrue(Inventory().check_product_quantity(46))
        self.assertFalse(Inventory().check_product_quantity(37))

    def test_remove_product(self):
        self.create_products()
        Inventory().add_product(46)
        Inventory().remove_product(46)
        self.assertFalse(Inventory().check_product_quantity(46))

    def test_get_product_price(self):
         self.create_products()
         self.assertTrue(Inventory().get_product_price(46) == 70)

    def test_get_product_name(self):
        self.create_products()
        self.assertTrue(Inventory().get_product_name(46) == "PEPSI")

class VendingMachineCoinstest(TestCase):
    def test_add_coins(self):
        VendingMachineCoins().add_coins(10,2)
        self.assertTrue(VendingMachineCoins.coins[Coins(10)] == 2)

    def test_remove_coins(self):
        VendingMachineCoins().remove_coins(10,2)
        self.assertTrue(VendingMachineCoins.coins[Coins(10)] == 0)

        VendingMachineCoins().add_coins(10,1)
        VendingMachineCoins().remove_coins(10,2)
        self.assertTrue(VendingMachineCoins.coins[Coins(10)] == 0)


    
