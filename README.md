#Mini Banking Application
The Mini Banking Application is a Python-based project designed to simulate basic banking operations. It provides a simple yet functional interface for users to perform essential banking tasks such as creating accounts, depositing money, withdrawing funds, checking balances, and viewing transaction history. This application is ideal for educational purposes, helping users understand fundamental banking operations and basic Python programming concepts.

Key Features
Account Management:

Create New Account: Users can open new accounts by providing necessary details such as name, initial deposit, and a unique account number.
Delete Account: Users can close existing accounts if they are no longer needed.
Transactions:

Deposit Funds: Users can deposit money into their accounts.
Withdraw Funds: Users can withdraw money from their accounts, ensuring that the withdrawal does not exceed the available balance.
Transfer Funds: Users can transfer money between different accounts within the bank.
Balance Inquiry:

Users can check the current balance of their accounts at any time.
Transaction History:

Users can view a list of all transactions (deposits, withdrawals, transfers) made on their accounts.
Authentication:

Basic authentication to ensure that only authorized users can access and manage their accounts.
Technical Details
Language: Python
Data Storage: Simple text files or SQLite database for storing account information and transaction history.
User Interface: Command-line interface (CLI) for user interactions.
Modules and Components
Account Module:

Manages account creation, deletion, and basic account information storage.
Transaction Module:

Handles all types of transactions (deposits, withdrawals, transfers) and maintains transaction logs.
Authentication Module:

Ensures that users are authenticated before performing any operations.
User Interface Module:

Provides a CLI for users to interact with the application, including menus and prompts for various actions.
How to Use
Setting Up:

Download and install Python on your system.
Clone or download the Mini Banking Application project files.
Running the Application:

Navigate to the project directory in your terminal.
Run the main Python script to start the application: python main.py.
Interacting with the Application:

Follow the on-screen prompts to create accounts, deposit or withdraw funds, check balances, and view transaction history.
Example Workflow
Create Account:

The user selects the option to create a new account.
The application prompts for details such as name, initial deposit, and account number.
The account is created and stored in the system.
Deposit Funds:

The user selects the deposit option.
The application prompts for the account number and the amount to deposit.
The amount is added to the account balance, and the transaction is logged.
Withdraw Funds:

The user selects the withdrawal option.
The application prompts for the account number and the amount to withdraw.
The amount is deducted from the account balance, provided sufficient funds are available, and the transaction is logged.
Check Balance:

The user selects the balance inquiry option.
The application prompts for the account number and displays the current balance.
View Transaction History:

The user selects the option to view transaction history.
The application displays a list of all transactions for the specified account.
This Mini Banking Application serves as an excellent learning tool for those new to Python and interested in understanding the basics of banking operations.
