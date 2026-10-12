categories = ["Food", "Transport", "Books"]
expenses = []

def clean_category(category):
    """Remove whitespace,standardized capitalization and returns clean category"""
    return category.strip().title()

def validate_category(category,categories):
    """returns boolean based on whether category in categories"""
    return category in categories

def get_category(categories):
    """Keeps asking user until an acceptable input is given"""
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

def calculate_category_totals(expenses):
    category_totals={}
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]
        
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount    

    return category_totals

def total_categories(category_totals):
    return len(category_totals)

def display_summary(report_text):
   print(report_text)
def format_summary(category_totals,total_categories,total_amount):
    report=""
    for category in category_totals:
        report+=f"{category} : {category_totals[category]}\n"
    report+=f"Total categories: {total_categories}\n"
    report+=f"Total amount: {total_amount}"
    return report

def export_report(report_text):
    with open("expense_report.txt","w") as file:
        file.write(report_text)

for i in range(3):
    expense=get_expense(categories)
    add_expense(expenses,expense)
category_totals = calculate_category_totals(expenses)
total_categories = total_categories(category_totals)
total_amount = calculate_total(expenses)

report_text=format_summary(category_totals,total_categories,total_amount)
display_summary(report_text)
export_report(report_text)

