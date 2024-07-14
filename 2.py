class BankAccount:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount:.2f}. New balance: {self.balance:.2f}.")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount:.2f}. New balance: {self.balance:.2f}.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self) -> float:
        return self.balance

if __name__ == "__main__":
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    account = BankAccount(account_number, account_holder)

    print(f"Account created for {account_holder} with account number {account_number}.")

    while True:
        action = input("Deposit, Withdraw, or Check Balance? (type 'exit' to quit): ").lower()
        if action == 'deposit':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == 'check balance':
            print(f"Current balance: {account.get_balance():.2f}")
        elif action == 'exit':
            break
        else:
            print("Invalid action.")
