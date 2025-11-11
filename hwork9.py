# Base class: Account
class Account:
    def __init__(self, name, balance):
        # Protected attributes
        self._name = name
        self._balance = balance

    def display_details(self):
        """Display account holder's name and balance."""
        return f"Account Holder: {self._name}, Balance: ₹{self._balance:.2f}"

    def __add__(self, other):
        """Overload + operator to add balances of two accounts."""
        if isinstance(other, Account):
            return self._balance + other._balance
        return NotImplemented


# Subclass: SavingsAccount
class SavingsAccount(Account):
    def calculate_interest(self):
        """Calculate 5% interest for Savings Account."""
        return self._balance * 0.05


# Subclass: CurrentAccount
class CurrentAccount(Account):
    def calculate_interest(self):
        """Calculate 2% interest for Current Account."""
        return self._balance * 0.02


# --- Main Program ---
def main():
    # Create account objects
    savings = SavingsAccount("Ravi", 10000.0)
    current = CurrentAccount("Anjali", 15000.0)

    print("----- BANK ACCOUNT DETAILS -----\n")

    # Display Savings Account Details
    print("---- Savings Account ----")
    print(savings.display_details())
    print(f"Interest (5%): ₹{savings.calculate_interest():.2f}\n")

    # Display Current Account Details
    print("---- Current Account ----")
    print(current.display_details())
    print(f"Interest (2%): ₹{current.calculate_interest():.2f}\n")

    # Calculate and show total balance using + operator
    total_balance = savings + current
    print("---- Combined Account Summary ----")
    print(f"Total Balance (Ravi + Anjali): ₹{total_balance:.2f}")


# Run the program
main()
