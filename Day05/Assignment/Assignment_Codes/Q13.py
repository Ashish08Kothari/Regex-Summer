
balance = 10000

while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: Rs.{balance}")

    elif choice == '2':
        amount = float(input("Enter amount to deposit: Rs."))
        if amount > 0:
            balance += amount
            print(f"Rs.{amount} deposited successfully. New balance: Rs.{balance}")
        else:
            print("Please enter a valid amount.")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: Rs."))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"Rs.{amount} withdrawn successfully. Remaining balance: Rs.{balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Please enter a valid amount.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")