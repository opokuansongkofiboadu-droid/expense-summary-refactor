categories = ["Food", "Transport", "Books"]
expenses = []

def clean_category(category):
    return category.strip().title()
def validate_category(category,categories):
    return category in categories
def get_category(categories):
    while True:
        
        category=input("Enter your category: ")
        category=clean_category(category)

        if validate_category(category,categories):
            return category
        else:
            print("Category can't be found")

def validate_amount(amount):
    return amount >= 0
def get_amount():
    while True:
        try:
            amount=float(input("Enter amount here: "))
            if validate_amount(amount):
                return amount
            else:
                print("Amount can't be negative")
        except ValueError:
            print("Number is invalid.Try again")

def get_expense(categories):
    category=get_category(categories)
    amount=get_amount()

    expense={"category":category,"amount":amount}
    return expense

def add_expense(expenses,expense):
    expenses.append(expense)

def calculate_total(expenses):
    total=0
    for expense in expenses:
        total+=expense["amount"]
    return total

for i in range(3):
    expense=get_expense(categories)
    add_expense(expenses,expense)
print(expenses)
print(calculate_total(expenses))