class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        
        self.limit = capacity
        self.amount = 0

    def __str__(self):
        return self.amount * '🍪'

    def deposit(self, n):
        if (self.amount + n) > self.limit:
            raise ValueError
        self.amount += n

    def withdraw(self, n):
        if self.amount - n < 0:
            raise ValueError
        self.amount -= n

    @property
    def capacity(self):
        return self.limit

    @property
    def size(self):
        return self.amount
