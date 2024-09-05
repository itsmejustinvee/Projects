import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


logged_in_username = ""
is_admin = False  # Track if the logged in user is an admin

# Login UI
def create_login_window():
    global login_window
    login_window = tk.Toplevel(root)
    login_window.title("Login - JVBank")
    
    tk.Label(login_window, text="Enter your username").grid(row=0, column=0, padx=10, pady=10)
    global username_entry
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(login_window, text="Enter your PIN").grid(row=1, column=0, padx=10, pady=10)
    global pin_entry
    pin_entry = tk.Entry(login_window, show="*")  # Hides the pin input
    pin_entry.grid(row=1, column=1, padx=10, pady=10)
    
    login_button = tk.Button(login_window, text="Login", command=validate_login)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Login validation
def validate_login():
    global logged_in_username, is_admin
    username = username_entry.get().strip()
    pin = pin_entry.get().strip()
    
    try:
        with open('accounts.txt.txt', 'r') as file:
            users = file.readlines()
            login_successful = False
            
            for user in users:
                stored_username, stored_pin, balance, role = user.strip().split('*')  # Updated to include the role
                
                if username == stored_username and pin == stored_pin:
                    logged_in_username = username
                    is_admin = (role == "admin")  # Check if the user is an admin
                    login_successful = True
                    messagebox.showinfo("Account Verified", f"Hello, {username}. Thank you for using JVBank.")
                    login_window.destroy()
                    if is_admin:
                        show_admin_menu()  # Direct to admin menu
                    else:
                        show_main_menu()   # Direct to user menu
                    break
            
            if not login_successful:
                messagebox.showerror("Login Failed", "Invalid username or PIN. Usernames and passwords are case sensitive.")
                
    except FileNotFoundError:
        messagebox.showerror("ADMIN MESSAGE", "Missing accounts.txt")

# Main menu
def show_main_menu():
    main_menu = tk.Toplevel(root)
    main_menu.title("Main Menu")
    
    tk.Button(main_menu, text="Check Balance", command=check_balance).pack(padx=10, pady=10)
    tk.Button(main_menu, text="Deposit Money", command=deposit_money).pack(padx=10, pady=10)
    tk.Button(main_menu, text="Withdrawal Money", command=withdraw_money).pack(padx=10, pady=10)
    tk.Button(main_menu, text="Change PIN", command=change_pin).pack(padx=10, pady=10)
    tk.Button(main_menu, text="Exit", command=main_menu.destroy).pack(padx=10, pady=10)

# Admin menu
def show_admin_menu():
    admin_menu = tk.Toplevel(root)
    admin_menu.title("Admin Menu")
    
    tk.Button(admin_menu, text="View All Accounts", command=view_all_accounts).pack(padx=10, pady=10)
    tk.Button(admin_menu, text="Create Account", command=create_account_window).pack(padx=10, pady=10)
    tk.Button(admin_menu, text="Delete Account", command=delete_account_window).pack(padx=10, pady=10)
    tk.Button(admin_menu, text="Plot Account Balances", command=plot_balances).pack(padx=10, pady=10)
    
    def exit_admin_menu():
        admin_menu.destroy()
        create_login_window()
    
    tk.Button(admin_menu, text="Exit", command=exit_admin_menu).pack(padx=10, pady=10)
# Check balance
def check_balance():
    try:
        with open('accounts.txt.txt', 'r') as file:
            users = file.readlines()
            for user in users:
                stored_username, stored_pin, balance, role = user.strip().split('*')
                if logged_in_username == stored_username:
                    balance = balance.replace(',', '')  # Remove commas from balance
                    messagebox.showinfo("Check Balance", f"Your current balance is: ${float(balance):,.2f}")
                    return
    except FileNotFoundError:
        messagebox.showerror("ADMIN MESSAGE", "MISSING accounts.txt")

# Deposit $
def deposit_money():
    def process_deposit():
        amount = deposit_entry.get().replace(',', '').strip()  # Remove commas from balance
        try:
            amount = float(amount)
            if amount > 0:
                updated_users = []
                try:
                    with open('accounts.txt.txt', 'r') as file:
                        users = file.readlines()
                        for user in users:
                            stored_username, stored_pin, balance, role = user.strip().split('*')
                            if logged_in_username == stored_username:
                                balance = balance.replace(',', '')  # Remove commas again
                                new_balance = float(balance) + amount
                                updated_users.append(f"{stored_username}*{stored_pin}*{new_balance:,.2f}*{role}\n")
                                messagebox.showinfo("Deposit Successful", f"You have deposited ${amount:,.2f}. Your new balance is ${new_balance:,.2f}")
                            else:
                                updated_users.append(user)
                    with open('accounts.txt.txt', 'w') as file:
                        file.writelines(updated_users)
                    deposit_window.destroy()
                except FileNotFoundError:
                    messagebox.showerror("ADMIN MESSAGE", "MISSING FILE accounts.txt")
            else:
                messagebox.showerror("ERROR", "Please enter a positive amount for deposits.")
        except ValueError:
            messagebox.showerror("ERROR", "Please enter a valid number.")

    deposit_window = tk.Toplevel(root)
    deposit_window.title("Deposit Money")
    tk.Label(deposit_window, text="How much would you like to deposit?: ").pack(pady=10)
    deposit_entry = tk.Entry(deposit_window)
    deposit_entry.pack(pady=10)
    tk.Button(deposit_window, text="Deposit", command=process_deposit).pack(pady=10)

# Withdraw $
def withdraw_money():
    def process_withdrawal():
        amount = withdrawal_entry.get().replace(',', '').strip()
        try:
            amount = float(amount)
            if amount > 0 and amount <= 1000 and amount % 10 == 0:
                updated_users = []
                try:
                    with open('accounts.txt.txt', 'r') as file:
                        users = file.readlines()
                        for user in users:
                            stored_username, stored_pin, balance, role = user.strip().split('*')
                            if logged_in_username == stored_username:
                                balance = balance.replace(',', '')
                                current_balance = float(balance)
                                
                                if amount <= current_balance:
                                    new_balance = current_balance - amount
                                    updated_users.append(f"{stored_username}*{stored_pin}*{new_balance:,.2f}*{role}\n")
                                    messagebox.showinfo("Withdrawal Successful", f"You have withdrawn ${amount:,.2f}. Your new balance is ${new_balance:,.2f}")
                                else:
                                    messagebox.showerror("Insufficient Funds", "Insufficient funds, please check your balance.")
                                    updated_users.append(user)
                            else:
                                updated_users.append(user)
                    with open('accounts.txt.txt', 'w') as file:
                        file.writelines(updated_users)
                    withdrawal_window.destroy()
                except FileNotFoundError:
                    messagebox.showerror("ADMIN MESSAGE", "MISSING FILE accounts.txt")
            else:
                if amount > 1000:
                    messagebox.showerror("ERROR", "You can only withdraw a maximum of $1,000 per transaction.")
                elif amount % 10 != 0:
                    messagebox.showerror("ERROR", "Withdrawal amount must be in multiples of $10.")
                else:
                    messagebox.showerror("ERROR", "Please enter a positive amount for withdrawals.")
        except ValueError:
            messagebox.showerror("ERROR", "Please enter a valid number.")

    withdrawal_window = tk.Toplevel(root)
    withdrawal_window.title("Withdraw Money")
    tk.Label(withdrawal_window, text="How much would you like to withdraw?: ").pack(pady=10)
    withdrawal_entry = tk.Entry(withdrawal_window)
    withdrawal_entry.pack(pady=10)
    tk.Button(withdrawal_window, text="Withdraw", command=process_withdrawal).pack(pady=10)

# Change PIN
def change_pin():
    def process_pin_change():
        current_pin = current_pin_entry.get().strip()
        new_pin = new_pin_entry.get().strip()
        confirm_pin = confirm_pin_entry.get().strip()
        
        if new_pin.isdigit() and len(new_pin) == 4 and new_pin == confirm_pin:
            updated_users = []
            try:
                with open('accounts.txt.txt', 'r') as file:
                    users = file.readlines()
                    for user in users:
                        stored_username, stored_pin, balance, role = user.strip().split('*')
                        if logged_in_username == stored_username:
                            if current_pin == stored_pin:
                                updated_users.append(f"{stored_username}*{new_pin}*{balance}*{role}\n")
                                messagebox.showinfo("PIN Successfully Changed", "Your PIN has been updated.")
                            else:
                                messagebox.showerror("ERROR", "Invalid current PIN number.")
                                return
                        else:
                            updated_users.append(user)
                with open('accounts.txt.txt', 'w') as file:
                    file.writelines(updated_users)
                pin_window.destroy()
            except FileNotFoundError:
                messagebox.showerror("ADMIN MESSAGE", "MISSING FILE accounts.txt")
        else:
            if new_pin != confirm_pin:
                messagebox.showerror("ERROR", "Confirmation Invalid, ensure the new pin matches the confirmation.")
            else:
                messagebox.showerror("ERROR", "Please enter a 4 digit PIN")

    pin_window = tk.Toplevel(root)
    pin_window.title("Change PIN")
    tk.Label(pin_window, text="Enter your current PIN: ").pack(pady=10)
    current_pin_entry = tk.Entry(pin_window, show="*")
    current_pin_entry.pack(pady=5)
    
    tk.Label(pin_window, text="Enter a new 4 digit PIN: ").pack(pady=10)
    new_pin_entry = tk.Entry(pin_window, show="*")
    new_pin_entry.pack(pady=5)
    
    tk.Label(pin_window, text="Confirm your new PIN: ").pack(pady=10)
    confirm_pin_entry = tk.Entry(pin_window, show='*')
    confirm_pin_entry.pack(pady=5)
    
    tk.Button(pin_window, text="Change PIN", command=process_pin_change).pack(pady=10)
    
#ADMINISTRATIVE FUNCTIONS

# View all accounts
def view_all_accounts():
    try:
        with open('accounts.txt.txt', 'r') as file:
            users = file.readlines()
            user_info = "\n".join([user.strip() for user in users])
            messagebox.showinfo("Active Accounts", user_info)
    except FileNotFoundError:
        messagebox.showerror("ADMIN MESSAGE", "MISSING accounts.txt")

# Create accounts
def create_account_window():
    def create_account():
        new_username = username_entry.get().strip()
        new_pin = pin_entry.get().strip()
        initial_balance = balance_entry.get().strip()
        role = role_entry.get().strip().lower()

        if not new_username or not new_pin.isdigit() or len(new_pin) != 4:
            messagebox.showerror("ERROR", "Please enter a valid username and 4-digit PIN.")
            return

        if not initial_balance.replace('.', '', 1).isdigit() or float(initial_balance) < 0:
            messagebox.showerror("ERROR", "Please enter a valid initial balance.")
            return

        if role not in ['user', 'admin']:
            messagebox.showerror("ERROR", "Role must be 'user' or 'admin'.")
            return

        try:
            with open('accounts.txt.txt', 'a') as file:
                initial_balance = float(initial_balance)
                file.write(f"{new_username}*{new_pin}*{initial_balance:,.2f}*{role}\n")
                messagebox.showinfo("Account Created", f"Account for {new_username} has been created.")
                create_account_window.destroy()
        except FileNotFoundError:
            messagebox.showerror("ADMIN MESSAGE", "MISSING FILE accounts.txt")

    create_account_window = tk.Toplevel(root)
    create_account_window.title("Create Account")
    
    tk.Label(create_account_window, text="Username:").pack(pady=5)
    username_entry = tk.Entry(create_account_window)
    username_entry.pack(pady=5)
    
    tk.Label(create_account_window, text="PIN (4 digits):").pack(pady=5)
    pin_entry = tk.Entry(create_account_window, show="*")
    pin_entry.pack(pady=5)
    
    tk.Label(create_account_window, text="Initial Balance:").pack(pady=5)
    balance_entry = tk.Entry(create_account_window)
    balance_entry.pack(pady=5)
    
    tk.Label(create_account_window, text="Role (user/admin):").pack(pady=5)
    role_entry = tk.Entry(create_account_window)
    role_entry.pack(pady=5)
    
    tk.Button(create_account_window, text="Create Account", command=create_account).pack(pady=10)
    
#Delete account
def delete_account_window():
    def delete_account():
        delete_user = username_entry.get().strip()
        if not delete_user:
            messagebox.showerror("ERROR", "Please enter a valid username.")
            return
        
        try:
            with open('accounts.txt.txt', 'r') as file:
                users = file.readlines()
                
            updated_users = []
            account_found = False
            
            for user in users:
                stored_username, stored_pin, balance, role = user.strip().split('*')
                if stored_username != delete_user:
                    updated_users.append(user)
                else:
                    account_found = True
            
            if account_found:
                with open('accounts.txt.txt', 'w') as file:
                    file.writelines(updated_users)
                messagebox.showinfo("Account Deleted", f"You have successfully deleted {delete_user}.")
                delete_window.destroy()
            else:
                messagebox.showerror("ERROR", f"No account found for username: {delete_user}.")
                
        except FileNotFoundError:
            messagebox.showerror("ADMIN MESSAGE", "MISSING FILE accounts.txt")
            
#UI for deletion
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Account")

    tk.Label(delete_window, text="Enter the username you wish to delete: ").pack(pady=10)
    username_entry = tk.Entry(delete_window)
    username_entry.pack(pady=10)

    tk.Button(delete_window, text="Delete Account", command=delete_account).pack(pady=10)

#Plotting balances
    
def plot_balances():
    try:
        with open('accounts.txt.txt', 'r') as file:
            users = file.readlines()
            
        usernames = []
        balances = []
        
        for user in users:
            stored_username, stored_pin, balance, roles = user.strip().split('*')
            usernames.append(stored_username)
            balances.append(float(balance.replace(',', '')))
            
        if len(usernames) == 0:
            messagebox.showinfo("No Data", "There is no one to plot for.")
            return
        
        plt.figure(figsize=(10,5))
        plt.bar(usernames, balances, color='orange')
        plt.title('Who is the richest of them all?')
        plt.xlabel('Accounts')
        plt.ylabel('Cashmoney $')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        messagebox.showerror("ADMIN MESSAGE", "MISSING accounts.txt")
            

# Main app window
root = tk.Tk()
root.withdraw()

# Conjures the login window
create_login_window()
# Starts the main loop
root.mainloop()
