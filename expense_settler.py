import random
from sortedcontainers import SortedList

class User():
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def __str__(self):
        return f"User {self.id}, Balance: {self.balance}"

    def __lt__(self, other):
        return self.balance < other.balance

    

class Expense():
    def __init__(self, payer, creditor, amount):
        self.debtor = payer  # the one who pays
        self.creditor = creditor  # the one who receives
        self.amount = amount  # the amount of money transferred

    def __str__(self):
        return f"{self.debtor} gave {self.creditor} ${self.amount}"


def settle_up(expenses: list[Expense], group_size: int):
    # Prints all expenses
    print("\n".join(map(str,expenses)))
    print()

    # An array used to calculate users net balances
    net_balances = [0 for _ in range(group_size)]

    # Calculates a net balance for each user based on his expenses
    for expense in expenses:
        net_balances[expense.debtor] -= expense.amount
        net_balances[expense.creditor] += expense.amount

    # Prints the resulting array
    print(net_balances)
    print()

    # Edge case: All users are settled up
    if all(balance == 0 for balance in net_balances):
        print("All balances are already settled.")
        return []

    # Creates a list that allows us to insert, search and delete in O(log n)
    # This list is used to keep track of users' balances and generate an optimal money flow
    users = SortedList()

    # We add all the users and their corresponding balances to the list
    for i in range(len(net_balances)):
        if net_balances[i] != 0:
            users.add(User(i, net_balances[i]))

    # Result array returning all the transactions users have to perform to settle up their expenses
    transactions = []

    while len(users) >= 2:
        creditor = users.pop(0) # his balance is always negative
        debtor = users.pop(-1) # his balance is always positive
        print(f"Creditor: {creditor}, Debtor: {debtor}")

        # Since creditor's balance is always negative we sum their balances to get the difference between them
        new_balance = creditor.balance + debtor.balance
        transaction_value = min(debtor.balance, abs(creditor.balance))
        
        # We add the transaction to the result list
        if transaction_value > 0:
            transactions.append(Expense(debtor.id, creditor.id, transaction_value))

        # We don't want to add back users with 0 balance to the list
        if new_balance == 0:
            continue

        if abs(creditor.balance) > debtor.balance:
            users.add(User(creditor.id, new_balance))  # We add the creditor back to the list as he hasn't received all his money yet
        else:
            users.add(User(debtor.id, new_balance))  # We add the debtor back to the list as he still has debts to pay
        

    print()
    print("\n".join(map(str,transactions)))

    return transactions  


expense_log =[]
users_count = 3
for i in range(3):
    payer = random.randint(0,users_count-1)
    borrower = random.randint(0,users_count-1)
    value = random.randint(0, 100)
    expense_log.append(Expense(payer, borrower, value))


settle_up(expense_log, users_count)