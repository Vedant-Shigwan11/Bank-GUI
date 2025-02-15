import tkinter as tk
from tkinter import messagebox

class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}"

class BankingSystem:
    def __init__(self, root):
        self.accounts = {}
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        title_label = tk.Label(root, text="Banking System", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)

        self.create_account_frame = tk.LabelFrame(root, text="Create Account", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#d9edf7")
        self.create_account_frame.pack(pady=10, fill="both")
        
        self.create_entry_widgets(self.create_account_frame)

        self.transaction_frame = tk.LabelFrame(root, text="Transactions", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#dff0d8")
        self.transaction_frame.pack(pady=10, fill="both")
        
        self.create_transaction_widgets(self.transaction_frame)
        
        self.info_frame = tk.LabelFrame(root, text="Account Info", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#fcf8e3")
        self.info_frame.pack(pady=10, fill="both")
        
        self.create_info_widgets(self.info_frame)
    
    def create_entry_widgets(self, frame):
        tk.Label(frame, text="Account Number:", bg="#d9edf7").grid(row=0, column=0)
        self.acc_num_entry = tk.Entry(frame)
        self.acc_num_entry.grid(row=0, column=1)

        tk.Label(frame, text="Account Holder:", bg="#d9edf7").grid(row=1, column=0)
        self.acc_holder_entry = tk.Entry(frame)
        self.acc_holder_entry.grid(row=1, column=1)

        tk.Label(frame, text="Initial Balance:", bg="#d9edf7").grid(row=2, column=0)
        self.initial_balance_entry = tk.Entry(frame)
        self.initial_balance_entry.grid(row=2, column=1)

        tk.Button(frame, text="Create Account", command=self.create_account, bg="#31708f", fg="white").grid(row=3, columnspan=2, pady=5)

    def create_transaction_widgets(self, frame):
        tk.Label(frame, text="Account Number:", bg="#dff0d8").grid(row=0, column=0)
        self.trans_acc_num_entry = tk.Entry(frame)
        self.trans_acc_num_entry.grid(row=0, column=1)

        tk.Label(frame, text="Amount:", bg="#dff0d8").grid(row=1, column=0)
        self.amount_entry = tk.Entry(frame)
        self.amount_entry.grid(row=1, column=1)

        tk.Button(frame, text="Deposit", command=self.deposit, bg="#3c763d", fg="white").grid(row=2, column=0, pady=5)
        tk.Button(frame, text="Withdraw", command=self.withdraw, bg="#8a6d3b", fg="white").grid(row=2, column=1, pady=5)

    def create_info_widgets(self, frame):
        tk.Label(frame, text="Account Number:", bg="#fcf8e3").grid(row=0, column=0)
        self.info_acc_num_entry = tk.Entry(frame)
        self.info_acc_num_entry.grid(row=0, column=1)

        tk.Button(frame, text="Display Info", command=self.display_info, bg="#8a6d3b", fg="white").grid(row=1, columnspan=2, pady=5)

    def create_account(self):
        acc_num = self.acc_num_entry.get()
        acc_holder = self.acc_holder_entry.get()
        try:
            initial_balance = float(self.initial_balance_entry.get())
        except ValueError:
            messagebox.showwarning("Error", "Invalid balance amount!")
            return

        if acc_num and acc_holder:
            self.accounts[acc_num] = Account(acc_num, acc_holder, initial_balance)
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showwarning("Error", "Account number and holder name cannot be empty!")

    def deposit(self):
        acc_num = self.trans_acc_num_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showwarning("Error", "Invalid deposit amount!")
            return

        if acc_num in self.accounts:
            try:
                self.accounts[acc_num].deposit(amount)
                messagebox.showinfo("Success", f"Deposited {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            except ValueError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Account not found!")

    def withdraw(self):
        acc_num = self.trans_acc_num_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showwarning("Error", "Invalid withdrawal amount!")
            return

        if acc_num in self.accounts:
            try:
                self.accounts[acc_num].withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            except (InsufficientFundsError, ValueError) as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Account not found!")

    def display_info(self):
        acc_num = self.info_acc_num_entry.get()
        if acc_num in self.accounts:
            messagebox.showinfo("Account Info", self.accounts[acc_num].display_account_info())
        else:
            messagebox.showwarning("Error", "Account not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()
