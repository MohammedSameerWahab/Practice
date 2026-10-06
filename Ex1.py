class Atm:

    def __init__(self):
        self.balance = 0
        self.pin = None

    def menu(self):
        while True:
            user_input = input(
                f"""
Welcome to the {self.__class__.__name__} ATM.
Select your desired option:

1 - Create Pin
2 - Check Balance
3 - Make Deposit
4 - Make Withdrawal
5 - Exit
"""
            )

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.check_balance()

            elif user_input == "3":
                self.make_deposit()

            elif user_input == "4":
                self.make_withdrawal()

            elif user_input == "5":
                print("Bye!")
                break

            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        self.pin = input("Set your pin: ")
        print("PIN created successfully.")

    def check_pin(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return False

        ip_pin = input("Enter the pin: ")

        if ip_pin == self.pin:
            return True

        return False

    def check_balance(self):
        if self.check_pin():
            print(f"Your balance is: ₹{self.balance}")
        else:
            print("Invalid PIN!")

    def make_deposit(self):
        if self.check_pin():
            amount = int(input("Enter the amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                self.balance += amount
                print("Deposit successful.")

    def make_withdrawal(self):
        if self.check_pin():
            amount = int(input("Enter the amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")

            elif amount > self.balance:
                print("Insufficient funds in your account!")

            else:
                self.balance -= amount
                print("Transaction successful.")


smr = Atm()
smr.menu()
