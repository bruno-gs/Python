class BankAccount:
    apr = 1.2

print(BankAccount.__dict__) # {'__module__': '__main__', 'apr': 1.2, '__dict__': <attribute '__dict__' of 'BankAccount' objects>, '__weakref__': <attribute '__weakref__' of 'BankAccount' objects>, '__doc__': None}
print()
print(BankAccount.apr)      # 1.2

acc_1 = BankAccount()
acc_2 = BankAccount()

print(acc_1 is acc_2)       # False

print(acc_1.__dict__, acc_2.__dict__)   # {} {}

print(acc_1.apr, acc_2.apr) # 1.2 1.2

BankAccount.account_type = 'Savings'

print(acc_1.account_type, acc_2.account_type) # Savings Savings

acc_1.apr = 0

print(acc_1.__dict__, acc_2.__dict__)   # {'apr': 0} {}

# Look first in the instance, in this case, acc_1 has a new value for apr, then it returns. acc_2 keep using from the class
print(acc_1.apr, acc_2.apr) # 0 1.2

setattr(acc_2, 'apr', 10)

print(acc_2.__dict__)   # {'apr': 10}

print(getattr(acc_2, 'apr'))    # 10

acc_3 = BankAccount()
print(getattr(acc_3,'apr'))      # 1.2

acc_1.bank = 'Acme Savings & Loans'
print(acc_1.__dict__)   # {'apr': 0, 'bank': 'Acme Savings & Loans'}

class Program:
    language = 'Python'

p = Program()
print(p.__dict__)   # {}

p.__dict__['version'] = '3.8'
print(p.__dict__)   # {'version': '3.8'}

print(p.version)                # 3.8
print(getattr(p, 'version'))    # 3.8

p2 = Program()
p2.version = '3.7'
print(p2.__dict__)  # {'version': '3.7'}

