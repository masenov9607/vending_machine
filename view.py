import models
import controller
from utils import Singleton
from utils import Coins

class VendingMachineView(metaclass=Singleton):
    def throw_product(self,order):
        #give the product to the client
        pass

    def display_message(self,message):
        #print message to vending machine display
        print(message)

    def choose_product(self,code):
        #Calculate the code from the buttons
        self.code = code
        self.display_message("Insert money")

    def collect_money(self,money):
        order = Order(self.code,money)
        VendingMachineController(self.code,money).get_product(order)

    def insert_product(self,code,amount):
        VendingMachineController().push_product(code,amount)