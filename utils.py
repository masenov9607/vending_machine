import enum
import models
class Coins(enum.IntEnum):
    TEN_COINS = 10
    TWENTY_COINS = 20
    FIFTY_COINS = 50
    HUNDRED_COINS = 100

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



class CalculatorChange(metaclass=Singleton):
    def coinChange(self, coins, amount):
        
        def backtrack(amount=amount,count=0,start=0,path=[]):
            if amount == 0:
                if self.mincoin > count:
                    self.res = path
                    self.mincoin = count
            elif amount > 0:
                for i in range(start,len(coins)):
                    if coins[i][1] > 0:
                        coins[i][1] -= 1
                        backtrack(amount - coins[i][0], count + 1, i, path + [coins[i][0]] )
                        coins[i][1] += 1
                        
                         
        self.mincoin = float("inf")
        self.res = []
        coins.sort(key=lambda x: x[0],reverse=True)
        backtrack()
        return self.res 