Version: Python 3.6.4
No external packages used.
Please find Git repo at:  https://github.com/OllyAtkinson/bambank_solution

Run file main.py to access program.  
Program currently runs in a terminal as a Python file, however could be further adapted to a web app using React/Flask/JavaScript/SQL.

Account ID's that are stored in the dict and can be used with the program:
-1234567
-1111111
-9876543
-7654321
(or select N to account and an account will be created for you)

Assumptions:
-Passwords are not needed for any transaction within the web app, however have potential as 'bamboo' is password by default stored in the bank_dict 
-There is no charge for transactions 
-No interest rates or taxes apply to the bank 
-It is not possible to transfer to accounts not stored in the dict of Bambank
-No overdraft; users can only transfer what they have got in their account
-If the user has not got an account, an account is created for the user by default
-Transfer amount must be greater than 0
-Negative 'deposit' not allowed

Edge Cases Considered:
-User transferring a value <= 0
-User depositing a value <= 0
-User transferring more than their account balance
-User inputing account ID that does not exist in Bambank dict




Example Output:

Welcome to Bambank, do you already have an account? (Y/N): Y
Please enter your account ID: 1234567
What do you require to do:
                            Check Balance, press B.
                            Send Bambeuros,  press S.
                            Deposit, press D.
                            Check Transactions, press T.
                            Exit Service,  press E.
                            B
15000 Bambeuros.
What do you require to do:
                            Check Balance, press B.
                            Send Bambeuros,  press S.
                            Deposit, press D.
                            Check Transactions, press T.
                            Exit Service,  press E.
                            S
What is the account ID to transfer to?: 1111111
How much do you want to transfer?: 250
Transfer successful and balance updated.
What do you require to do:
                            Check Balance, press B.
                            Send Bambeuros,  press S.
                            Deposit, press D.
                            Check Transactions, press T.
                            Exit Service,  press E.
                            D
How much would you like to deposit?: 1800
What do you require to do:
                            Check Balance, press B.
                            Send Bambeuros,  press S.
                            Deposit, press D.
                            Check Transactions, press T.
                            Exit Service,  press E.
                            T
0: 1111111 has been sent 250 Bambeuros. Your new balance is: 14750 Bambeuros.
1: You have deposited 1800 Bambeuros. Your new balance is: 16550 Bambeuros.
What do you require to do:
                            Check Balance, press B.
                            Send Bambeuros,  press S.
                            Deposit, press D.
                            Check Transactions, press T.
                            Exit Service,  press E.
                            E
Thanks for using Bambank, goodbye!


