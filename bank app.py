import tkinter as tk
from tkinter import messagebox

# Base class for a generic bank account
class Account:
    def __init__(self, owner, age, balance=0, password=""):
        self.owner = owner
        self.age = age
        self.balance = balance
        self._password = password

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def set_password(self, password):
        self._password = password

    def change_password(self, old_password, new_password):
        if self._password == old_password:
            self._password = new_password
            return True
        else:
            return False

    def check_password(self, password):
        return self._password == password

# Savings account class
class SavingsAccount(Account):
    INTEREST_RATE = 0.005  # 0.5% interest rate
    WITHDRAWAL_LIMIT = 700000

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.INTEREST_RATE
        self.balance += interest

    def withdraw(self, amount):
        if amount > self.WITHDRAWAL_LIMIT:
            return False
        return super().withdraw(amount)

# Current account class
class CurrentAccount(Account):
    pass  # No restrictions

# Children's account class
class ChildrensAccount(Account):
    INTEREST_RATE = 0.007  # 0.7% interest rate

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.INTEREST_RATE
        self.balance += interest

    def withdraw(self, amount):
        return False  # No withdrawals allowed

# Students account class
class StudentsAccount(Account):
    WITHDRAWAL_LIMIT = 2000
    DEPOSIT_LIMIT = 50000

    def deposit(self, amount):
        if amount > self.DEPOSIT_LIMIT:
            return False
        super().deposit(amount)
        return True

    def withdraw(self, amount):
        if amount > self.WITHDRAWAL_LIMIT:
            return False
        return super().withdraw(amount)

# Tkinter GUI application
class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingham Bank")

        self.account_types = {
            "Savings": SavingsAccount,
            "Current": CurrentAccount,
            "Children's": ChildrensAccount,
            "Student's": StudentsAccount
        }

        self.accounts = {}  # To store all accounts
        self.current_account = None  # To store the currently logged in account

        self.create_welcome_screen()

    def create_welcome_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="WELCOME TO BINGHAM BANK", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2)

        self.login_btn = tk.Button(self.root, text="Login", command=self.create_login_screen)
        self.login_btn.grid(row=1, column=0)

        self.signup_btn = tk.Button(self.root, text="Sign Up", command=self.create_signup_screen)
        self.signup_btn.grid(row=1, column=1)

    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Login", font=("Arial", 16)).grid(row=0, column=0, columnspan=2)

        tk.Label(self.root, text="Name:").grid(row=1, column=0)
        self.login_name = tk.Entry(self.root)
        self.login_name.grid(row=1, column=1)

        tk.Label(self.root, text="Account Number:").grid(row=2, column=0)
        self.login_account_number = tk.Entry(self.root)
        self.login_account_number.grid(row=2, column=1)

        tk.Label(self.root, text="Password:").grid(row=3, column=0)
        self.login_password = tk.Entry(self.root, show="*")
        self.login_password.grid(row=3, column=1)

        self.login_btn = tk.Button(self.root, text="Login", command=self.login)
        self.login_btn.grid(row=4, column=1)

        self.back_btn = tk.Button(self.root, text="Back", command=self.create_welcome_screen)
        self.back_btn.grid(row=4, column=0)

    def create_signup_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Sign Up", font=("Arial", 16)).grid(row=0, column=0, columnspan=2)

        tk.Label(self.root, text="Name:").grid(row=1, column=0)
        self.signup_name = tk.Entry(self.root)
        self.signup_name.grid(row=1, column=1)

        tk.Label(self.root, text="Age:").grid(row=2, column=0)
        self.signup_age = tk.Entry(self.root)
        self.signup_age.grid(row=2, column=1)

        tk.Label(self.root, text="BVN:").grid(row=3, column=0)
        self.signup_bvn = tk.Entry(self.root)
        self.signup_bvn.grid(row=3, column=1)

        tk.Label(self.root, text="Password:").grid(row=4, column=0)
        self.signup_password = tk.Entry(self.root, show="*")
        self.signup_password.grid(row=4, column=1)

        self.signup_btn = tk.Button(self.root, text="Sign Up", command=self.signup)
        self.signup_btn.grid(row=5, column=1)

        self.back_btn = tk.Button(self.root, text="Back", command=self.create_welcome_screen)
        self.back_btn.grid(row=5, column=0)

    def create_account_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Owner name
        tk.Label(self.root, text="Owner Name:").grid(row=0, column=0)
        self.owner_name = tk.Entry(self.root)
        self.owner_name.grid(row=0, column=1)

        # Age
        tk.Label(self.root, text="Age:").grid(row=1, column=0)
        self.age = tk.Entry(self.root)
        self.age.grid(row=1, column=1)

        # Account type
        tk.Label(self.root, text="Account Type:").grid(row=2, column=0)
        self.account_type = tk.StringVar()
        self.account_type.set("Savings")
        tk.OptionMenu(self.root, self.account_type, *self.account_types.keys()).grid(row=2, column=1)

        # Initial balance
        tk.Label(self.root, text="Initial Balance:").grid(row=3, column=0)
        self.initial_balance = tk.Entry(self.root)
        self.initial_balance.grid(row=3, column=1)

        # Password
        tk.Label(self.root, text="Password:").grid(row=4, column=0)
        self.password = tk.Entry(self.root, show="*")
        self.password.grid(row=4, column=1)

        # Create account button
        self.create_account_btn = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_btn.grid(row=5, column=1)

        # Action message
        self.action_msg = tk.Label(self.root, text="")
        self.action_msg.grid(row=6, column=0, columnspan=2)

        # Deposit
        tk.Label(self.root, text="Deposit Amount:").grid(row=7, column=0)
        self.deposit_amount = tk.Entry(self.root)
        self.deposit_amount.grid(row=7, column=1)
        self.deposit_btn = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_btn.grid(row=8, column=1)

        # Withdraw
        tk.Label(self.root, text="Withdraw Amount:").grid(row=9, column=0)
        self.withdraw_amount = tk.Entry(self.root)
        self.withdraw_amount.grid(row=9, column=1)
        self.withdraw_btn = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_btn.grid(row=10, column=1)

        # Display balance
        self.balance_label = tk.Label(self.root, text="Balance: $0")
        self.balance_label.grid(row=11, column=0, columnspan=2)

        # Change password
        tk.Label(self.root, text="Old Password:").grid(row=12, column=0)
        self.old_password = tk.Entry(self.root, show="*")
        self.old_password.grid(row=12, column=1)

        tk.Label(self.root, text="New Password:").grid(row=13, column=0)
        self.new_password = tk.Entry(self.root, show="*")
        self.new_password.grid(row=13, column=1)

        self.change_password_btn = tk.Button(self.root, text="Change Password", command=self.change_password)
        self.change_password_btn.grid(row=14, column=1)

    def signup(self):
        name = self.signup_name.get()
        age = int(self.signup_age.get())
        bvn = self.signup_bvn.get()
        password = self.signup_password.get()

        if age < 18:
            messagebox.showerror("Error", "Age must be at least 18.")
            return

        if len(bvn) != 10 or not bvn.isdigit():
            messagebox.showerror("Error", "BVN must be exactly 10 digits.")
            return

        # Store the user data
        self.accounts[bvn] = {"name": name, "age": age, "password": password}
        messagebox.showinfo("Success", "Sign up successful! Please log in to create an account.")
        self.create_welcome_screen()

    def login(self):
        name = self.login_name.get()
        account_number = self.login_account_number.get()
        password = self.login_password.get()

        if account_number in self.accounts and self.accounts[account_number]["password"] == password:
            self.current_account = self.accounts[account_number]
            messagebox.showinfo("Success", "Login successful!")
            self.create_account_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def create_account(self):
        owner = self.owner_name.get()
        age = int(self.age.get())
        balance = float(self.initial_balance.get())
        password = self.password.get()
        account_type = self.account_type.get()

        AccountClass = self.account_types[account_type]
        self.current_account["account"] = AccountClass(owner, age, balance, password)
        self.update_balance()
        self.action_msg.config(text=f"Created {account_type} account for {owner}")

    def deposit(self):
        if "account" in self.current_account:
            amount = float(self.deposit_amount.get())
            success = self.current_account["account"].deposit(amount)
            if not success:
                self.action_msg.config(text=f"Deposit failed. Exceeds limit.")
            else:
                self.update_balance()
                self.action_msg.config(text=f"Deposited ${amount}")
        else:
            self.action_msg.config(text="No account created.")

    def withdraw(self):
        if "account" in self.current_account:
            amount = float(self.withdraw_amount.get())
            success = self.current_account["account"].withdraw(amount)
            if not success:
                self.action_msg.config(text=f"Withdrawal failed. Exceeds limit or insufficient balance.")
            else:
                self.update_balance()
                self.action_msg.config(text=f"Withdrew ${amount}")
        else:
            self.action_msg.config(text="No account created.")

    def change_password(self):
        if "account" in self.current_account:
            old_password = self.old_password.get()
            new_password = self.new_password.get()
            if self.current_account["account"].change_password(old_password, new_password):
                self.action_msg.config(text="Password changed successfully")
            else:
                self.action_msg.config(text="Incorrect old password")
        else:
            self.action_msg.config(text="No account created.")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.current_account['account'].get_balance():.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()


