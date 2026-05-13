''' 
(1)   Class deep diving
(2) Encapsulation
(3) Inheritance
(4) Polimorphism
'''
print("======== Encapsulation ==========")
# Encapsulationda public private protected tushunchasi bor va u Pythonda
# Python > public,  __private,  _protected, shunaqa paztki chiziqcha bilan farqlanadi


class Account():
    # State
    description = "The class makes bank accounts"

    # Constructor
    def __init__(self, owner, amount):
        self.__owner = owner  # agarda _owner deb yozadigan bulsak uni private xolatga utgazgan bulamiz va tashqaridan tugridan tugri hack qilolmaydi
        # xuddi shunday _amount qilsak private buladi va xamma joyda shunaqa yozishimiz kk
        self.__amount = amount

    # Method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("* deposit executed *")
        self.__amount += amount

    def withdraw(self, amount):
        print(" Withdraw executed ")
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Tom", 5000)
my_account.get_balance()

print("-------")
my_account.deposit(3500)
my_account.withdraw(2400)
my_account.get_balance()

print("============")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)


print("owner before:", my_account.holder)  # state

# GETTER & SETTER
my_account.holder = "Shoxa"
print("owner after:", my_account.holder)
