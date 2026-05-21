# ===== PERSONAL EXPENSE TRACKER SYSTEM =====

def addExpense():

    try:
        date = input("ENTER DATE : ")
        category = input("ENTER CATEGORY : ")
        amount = int(input("ENTER AMOUNT : "))
        expense = f"{date},{category},{amount}\n"

        with open("expenses.txt","a") as f:
            f.write(expense)

        print("Transaction has been added successfully.")
    except Exception as e:
        print(e)

def viewExpenses():
    try:
        print("Displaying all recorded transactions:")
        with open("expenses.txt","r") as f:
            expenses = f.readlines()
            for expense in expenses:
                print(expense.strip().split(","))
    except FileNotFoundError as e:
        print(e)

def totalExpense():
    try:
        with open("expenses.txt","r") as f:
            expenseAmount = 0
            expenses = f.readlines()
            for expense in expenses:
                expense = expense.strip().split(",")
                expenseAmount += int(expense[2])
            print("Total amount spent: ",expenseAmount)
    except FileNotFoundError as e:
        print(e)

def searchByCategory():

    userCategory = input("ENTER YOUR CATEGORY : ")
    found = False

    try:
        with open("expenses.txt","r") as f:
            expenses = f.readlines()
            for expense in expenses:
                expense = expense.strip().split(",")
                if (expense[1].lower() == userCategory.lower()):
                    print(expense)
                    found = True
        if (found == False):
            print("No matching transaction records were found.")
    except FileNotFoundError as e:
        print(e)
        
while True:
    try:
        selection = int(input("===== PERSONAL EXPENSE TRACKER SYSTEM =====\n1. Add Expense\n2. View Expenses\n3. Total Expense\n4. Search by Category\n5. Exit\nENTER YOUR SELECTION : "))
    except Exception as e:
        print(e)
    if (selection == 1):
        addExpense()
    elif (selection == 2):
        viewExpenses()
    elif (selection == 3):
        totalExpense()
    elif (selection == 4):
        searchByCategory()
    elif (selection == 5):
        print("Thank you for using the Expense Tracker System. Goodbye!")
        break
    else:
        print("Invalid selection. Please choose a valid menu option.")
