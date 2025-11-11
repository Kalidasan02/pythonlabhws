from abc import ABC, abstractmethod

# Abstract Base Class
class User(ABC):
    def __init__(self, name, account_year):
        self._name = name
        self._account_year = account_year

    def account_age(self):
        """Return how many years old the account is (assuming current year is 2025)."""
        current_year = 2025
        return current_year - self._account_year

    @abstractmethod
    def get_role(self):
        """Abstract method that must be implemented by subclasses."""
        pass


# Subclass: Admin
class Admin(User):
    def get_role(self):
        """Return role for Admin."""
        return "Admin"

    def __str__(self):
        """User-friendly message for Admin."""
        return f"Admin Name: {self._name}, Account Age: {self.account_age()} years."


# Subclass: Guest
class Guest(User):
    def get_role(self):
        """Return role for Guest."""
        return "Guest"

    def __str__(self):
        """User-friendly message for Guest."""
        return f"Guest Name: {self._name}, Account Age: {self.account_age()} years."


# --- Main Program ---
def main():
    # Create objects for Admin and Guest
    admin_user = Admin("Ravi", 2020)
    guest_user = Guest("Anjali", 2023)

    # Display details
    print("----- WEBSITE USER DETAILS -----\n")

    print(f"Role: {admin_user.get_role()}")
    print(f"Account Age: {admin_user.account_age()} years")
    print(admin_user, "\n")

    print(f"Role: {guest_user.get_role()}")
    print(f"Account Age: {guest_user.account_age()} years")
    print(guest_user)


# Run the program
main()
