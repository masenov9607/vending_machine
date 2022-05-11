from models import Inventory
from models import VendingMachineCoins
import view
from utils import Singleton
from utils import Coins
from utils import CalculatorChange
from view import VendingMachineView
class VendingMachineController(metaclass=Singleton):


    def get_product(self,order):
        money_remained = order.get_collected_money() - Inventory().get_product_price(order._code)
        if money_remained >= 0:
            if Inventory().check_product_quantity(order._code):
                change = self.calculate_change(order)
                if  change != []:
                    for coin in change:
                        VendingMachineCoins().remove_coins(coin,1)
                    Inventory().remove_product(order._code)
                    VendingMachineView().throw_product(order)
                    VendingMachineView().display_message(f"Take your product {order.get_order_name()}")
                    return f"Take your product {order.get_order_name()}"
                else:
                    VendingMachineView().display_message("Not enough money to return")
                    return "Not enough money to return"
            else:
                VendingMachineView().display_message(f"No such product {order.get_order_name()}")
                return f"No such product {order.get_order_name()}"
        else:
            VendingMachineView().display_message(f"You need to enter extra {abs(money_remained)}")
            return f"You need to enter extra {abs(money_remained)}"

    def push_product(self,code,amount):
        for _ in range(amount):
            Inventory().add_product(code)

    def calculate_change(self,order):
        change = order.get_collected_money() - order.get_order_price()
        change_coins = []
        if change > 0:
            coins_freq = [[int(key),value] for key,value in VendingMachineCoins().coins.items()]
            change_coins = CalculatorChange().coinChange(coins_freq,change)
        return change_coins


            
       
        


