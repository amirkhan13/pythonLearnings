import os

FILENAME ="expenses.txt"


def load_expenses():
    if not  os.path.exists(FILENAME):
        return []
    
    expenses =[]

    with open(FILENAME,"r") as file:

        for line in file:
            name,amount,date,category=line.strip().split("|")

            expenses.append({
                "name":name,
                "amount":float(amount),
                "date":date,
                "category":category
            })            

        return expenses
    

def save_expense(expenses):
    with open(FILENAME,"w") as file:
        for expense in expenses:

            file.write(f"{expense['name']}|{expense['amount']}|{expense['date']}|{expense['category']}\n")


    
def add_expense(expenses):

    exp_name = input("Enter the Expense name:")
    exp_amount =float(input("Enter the expense amount:"))
    exp_date =input("Enter the expense date eg.(01-01-2001):")
    exp_category =input("Enter the expense category:")

    if not exp_name or not exp_date or not exp_category:
        print("Expense cannot be Empty or partially filled !! ")
        return 
    
    expenses.append({
        "name":exp_name,
        "amount":exp_amount,
        "date":exp_date,
        "category":exp_category
    })

    save_expense(expenses)
    print("Expense added Successfully!!")



def view_All_expense(expenses):

    if not expenses:
        print("No Expenses to show!!")
        return

    print("---Your Expenses--")
    for i, expense in enumerate(expenses,start=1):
        print(f"{i}. {expense['name']} | {expense['amount']} | {expense['date']} |{expense['category']}")


def view_monthly_expense(expenses):

    month = input("Enter the month of the expense to view e.g 01:")

    print(f"\n Expense for the Month {month}:\n")

    found=False
    for expense in expenses:
  
        expense_month = expense['date'].split("-")[1]


        if expense_month == month:
            found = True

            print(
                f"{expense['name']} | {expense['amount']} | {expense['date']} | {expense['category']}"
            )
            
        
    if not found:
        print("No expenses found for this month!!")
        
        

def main():

    expenses = load_expenses()
    while True:

        print("\n--- EXPENSE TRACKER CLI --- ")
        print("1.Add Expense:")
        print("2.View All Expenses:")
        print("3.View Monthly Expenses:")
        print("4.Exit")
        
        choice =input("Enter the Choice:")

        if choice =="1":
            add_expense(expenses)
        elif choice=="2":
            view_All_expense(expenses)
        elif choice =="3":
            view_monthly_expense(expenses)
        elif choice =="4":
            print("Sayonara!!!")
            break
        else:
            print("Invalid Choice!!")
        
main()



        

   
