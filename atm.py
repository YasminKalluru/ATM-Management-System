print("=" * 40)
print("      ATM MANAGEMENT SYSTEM")
print("=" * 40)
print("Welcome!")
print("=" * 40)

# Initial account details
balance = 5000
pin = 1234

# User login
entered_pin = int(input("Enter your 4-digit PIN: "))

# PIN Verification
if entered_pin == pin:

    print("\n✅ Login Successful!")

    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("==============================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"\nCurrent Balance: ₹{balance}")

    elif choice == 2:
        deposit_amount = int(input("Enter amount to deposit: ₹"))

        balance = balance + deposit_amount

        print("\n✅ Deposit Successful!")
        print(f"Updated Balance: ₹{balance}")

    elif choice == 3:
        withdraw_amount = int(input("Enter amount to withdraw: ₹"))

        if withdraw_amount <= balance:
            balance = balance - withdraw_amount
            print("\n✅ Withdrawal Successful!")
            print(f"Remaining Balance: ₹{balance}")
        else:
            print("\n❌ Insufficient Balance!")

    elif choice == 4:
        print("\nThank you for using our ATM!")

    else:
        print("\n❌ Invalid Menu Choice!")

else:
    print("\n❌ Invalid PIN!")


