class Account:

    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance

    def deposit_amount(self, dep_amount):
        self.balance = self.balance + dep_amount

    def with_amount(self, wth_amount):
        if self.balance > wth_amount:
            self.balance = self.balance - wth_amount
            print('Withdrawal accepted')
        else:
            print('Sorry')

    def __str__(self):
        return f"Owner: {self.owner} and \nBalanace : {self.balance}"


my_account = Account("Nupur", 1000)
my_account.deposit_amount(5000)
print(my_account)
my_account.with_amount(8000)
