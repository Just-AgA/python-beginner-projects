def withdraw():
    print("****************************")
    amount = float(input("Enter the amount to be withrawn: "))
    print("****************************")
    global balance 
    if amount > balance:
        print("****************************")
        print("You don't have enough money in your account to make this withdrawal")
        print("****************************")
        return 0
    elif amount < 0:
        print("****************************")
        print("Amount must be greater than 0")
        print("****************************")
        return 0
    balance -= amount
    print("****************************")
    print(f"You withdrew ${amount:.2f} from your account. Your balance is now ${balance:.2f}")
    print("****************************")

def show_balance():
    global balance
    balance = float(balance)
    print("****************************")
    print(f"Your balance is ${balance:.2f}")
    print("****************************")

def deposit():
    print("****************************")
    amount = float(input("Enter the amount to be deposited: "))
    print("****************************")

    if amount < 0:
        print("****************************")
        print("That is not a valid amount")
        print("****************************")
        return 0
    global balance 
    balance += amount
    print("****************************")
    print(f"You deposited ${amount} into your account. Your balance is now ${balance:.2f}")
    print("****************************")

is_running = True
balance = 0

while is_running:
    print("Banking program")
    print("1.Withdraw")
    print("2.Show balance")
    print("3.Deposit")
    print("4.Exit")

    print("****************************")
    choice = input("Enter an option: ")
    print("****************************")

    if choice == "1":
        withdraw()
    elif choice == "2":
        show_balance()
    elif choice == "3":
        deposit()
    elif choice == "4":
        is_running = False
    else:
        print("****************************")
        print("Please enter a valid option")
        print("****************************")

print("****************************")
print("Thank you. Have a great day!")
print("****************************")