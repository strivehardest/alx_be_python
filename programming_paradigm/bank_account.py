class BankAccount:
    """A simple BankAccount class that encapsulates banking operations."""
    
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance.
        
        Args:
            initial_balance (float): Starting balance (default 0.0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            bool: True if withdrawal succeeded, False otherwise
        """
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")