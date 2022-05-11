from utils import Singleton
from utils import Coins
class Product:

    def __init__(self,name,price,code):
        self._code = code
        self._name = name
        self._price = price if price > 0 else 0
        self._quantity = 0

class Order:
    def __init__(self,code,collected_cash):
        self._code = code
        self._money = collected_cash

    def get_order_name(self):
        return Inventory().get_product_name(self._code)

    def get_order_price(self):
        return Inventory().get_product_price(self._code)

    def get_collected_money(self):
        return self._money

class Inventory(metaclass=Singleton):
    _products = {}

    def get_product_price(self,code):
        product = self._products.get(code)
        price = 0
        if product:
            price = product._price
        return price

    def get_product_name(self,code):
        product = self._products.get(code)
        name = 0
        if product:
            name = product._name
        return name

    def add_product(self,code):
        if code in self._products:
            self._products[code]._quantity += 1

    def remove_product(self,code):
        if code in self._products:
            self._products[code]._quantity -= 1

    def check_product_quantity(self,code):
         if code in self._products:
            return self._products[code]._quantity > 0
    def get_product_quantity(self,code):
         if code in self._products:
            return self._products[code]._quantity



class VendingMachineCoins(metaclass=Singleton):
    coins = {Coins.TEN_COINS: 0,Coins.TWENTY_COINS: 0,Coins.FIFTY_COINS: 0,Coins.HUNDRED_COINS: 0}

    def add_coins(self,coin,amount):
        if Coins(coin) in self.coins:
            self.coins[Coins(coin)] += amount

    def remove_coins(self,coin,amount):
        if Coins(coin) in self.coins:
            self.coins[Coins(coin)] = max(0,self.coins[Coins(coin)] - amount)

    def get_total_amount(self):
        return sum(list(self.coins.values()))

