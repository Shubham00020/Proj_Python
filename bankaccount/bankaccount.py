class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "This account belongs to %s the available balance in the account is %.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "The available balance is %.2f" % (self.balance)
  
  def deposit(self, amount):
    if amount < 0:
      print "Invalid amount"
      return
    else:
      print "The amount u r depositing is %.2f" % (amount)
      self.balance += amount
      self.show_balance()
  
  def withdraw(self, amount):
    if amount > self.balance:
      print "U don't have that much money"
      return
    else:
      print "The amount u r withdrawing is %.2f" % (amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("shubham")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account