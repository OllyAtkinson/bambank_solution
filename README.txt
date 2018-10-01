Version: Python 3.6.4
No external packages used.
Please find Git repo at:  https://github.com/OllyAtkinson/bambank_solution

Run file main.py to access program.  
Program currently runs in a terminal as a Python file, however could be further adapted to a web app using React/Flask/JavaScript/SQL.  

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


