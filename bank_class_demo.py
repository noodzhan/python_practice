import bank_class
acct = bank_class.Account('zhihu','123-4567',1000)
acct.deposit(500)
acct.withdraw(100)
print(acct)
acct.balance=1000
print(acct)