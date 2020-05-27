from abc import ABC, abstractmethod
class bike(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)

    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(bike):
    def payment(self, amount):
        print('Your total purchase amount was {}'.format(amount))

obj = DebitCardPayment()
obj.paySlip("$300")
obj.payment("$300")
