import collections
class TransactionHandler(object):

    def __init__(self, stock, orders):
        self.stock = stock
        self.orders = orders
        self.dollarsEarned = 0

    def isInStock(self, order):
        if self.stock[order[0]]:
            return True
        else: return False

    def removeFromStock(self, order):
        self.stock.subtract(order)

    def receivePayment(self, order):
        self.dollarsEarned += int(order[1])

    def handleOrders(self):
        for order in self.orders:
            if self.isInStock(order):
                self.removeFromStock(order)
                self.receivePayment(order)

    def showDollarsEarned(self):
        print(self.dollarsEarned)

x, stock, n  = int(input()), collections.Counter(input().split()), int(input())
customerOrders = [input().split() for i in range(n)]

raghusOrder = TransactionHandler(stock, customerOrders)
raghusOrder.handleOrders()
raghusOrder.showDollarsEarned()
