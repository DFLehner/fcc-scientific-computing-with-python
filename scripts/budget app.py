from math import floor

#Budget app that generates a ledger for categories of spending and validates whether withdrawals can be made based
#on balance. Underneath a function to track outgoing expenditure of several categories.

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.outgoing = 0


    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        return False

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description':description})
        self.balance -= amount
        self.outgoing += amount
        return True
    def get_balance(self):
        return self.balance
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount=amount, description='Transfer to %s' % (category.name))
        self.outgoing -= amount
        category.deposit(amount=amount, description='Transfer from %s' % (self.name))
        return True
    
    def __repr__(self):
        string = self.name.center(30, '*')
        
        for entry in self.ledger:
            string += '\n'
            formatted_description = entry['description'][:23].ljust(23,' ')
            formatted_amount = f"{entry['amount']:.2f}".rjust(7,' ')
            string += formatted_description + formatted_amount
            
        string += '\nTotal: %s' % self.balance
        return string

    pass


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)
auto = Category('Auto')
auto.deposit(100)
auto.withdraw(50)
def create_spend_chart(categories):
    graph = 'Percentage spent by category\n'
    labels = ''
    total_outgoing = 0
    for category in categories:
        total_outgoing += category.outgoing
    for i in range(10, -1, -1):
        graph += str(10*i).rjust(3,' ') + '| '
        longest_category = 0
        names = []
        for category in categories:
            

            if floor(100*category.outgoing/(10*total_outgoing))*10 >= 10*i:
                graph += 'o  '
            else:
                graph += '   '

        graph += '\n'
    graph += '    -' + ''.ljust(len(categories)*3,'-') + '\n'
    for category in categories:
        longest_category = max(len(category.name), longest_category)
        names.append(category.name.ljust(30,' '))
    
    for i in range(0,longest_category):
        labels += '     '
        for name in names:
            labels += name[i] + '  '
        labels += '\n'
    #labels = labels[:-1]    
    graph += labels
    return graph[:-1]


    pass

print(create_spend_chart([food, clothing, auto]))