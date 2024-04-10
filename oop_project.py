from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Iyke = BankAccount(200000, "Iyke")
Sara = BankAccount(2000, "Sara")

Dave.deposit(200)
Dave.withdraw(20)

Dave.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingAccount(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Sara)