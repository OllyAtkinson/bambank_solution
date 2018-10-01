import random


class Bank:


    def __init__(self, account_number, balance=100):
        self.account_number = account_number
        self.balance = balance


    def bank_database():
        bank_dict = {'1234567':[15000, 'bamboo'],
                     '1111111':[1800, "bamboo"],
                     '9876543':[5, 'bamboo'],
                     '7654321':[9999, 'bamboo']}
        return bank_dict


    def check_balance(account_number, bank_dict):
        bank_balance = (bank_dict[account_number][0])
        return bank_balance


    def deposit(deposit_amount, account_number, bank_dict, trans_list):
        #print (deposit_amount)
        (bank_dict[account_number][0]) = ((bank_dict[account_number][0])  + deposit_amount)
        trans_list.append("You have deposited " + str(deposit_amount) + " Bambeuros. Your new balance is: " + str(bank_dict[account_number][0]) + " Bambeuros.")
        return bank_dict, trans_list


    def transfer(account_number, bank_dict, transfer_amount, transfer_contact, trans_list):

        transfer_contact = str(transfer_contact)
        if (bank_dict[account_number][0]) > transfer_amount:
            if transfer_contact in bank_dict:
                (bank_dict[account_number][0]) = ((bank_dict[account_number][0])  - transfer_amount)
                (bank_dict[transfer_contact][0]) = ((bank_dict[transfer_contact][0]) + transfer_amount)
                print("Transfer successful and balance updated")
                trans_list.append(str(transfer_contact) + " has been sent " + str(transfer_amount) + " Bambeuros. Your new balance is: " + str(bank_dict[account_number][0]) + " Bambeuros.")
            else:
                print("Account number does not exist")
        else:
            print("Insufficient funds to make that transfer.")
        return bank_dict


    def transactions():
        trans_list = []
        return trans_list


    def get_account_by_number(account_number, bank_dict):
        if account_number in bank_dict:
            bank_balance = (bank_dict[account_number][0])
        else:
            print("I'm sorry but your account hasn't been recognised.")
            main()
        return bank_balance


    def add_an_account(account_number, bank_dict):
        balance = 100
        password = 'bamboo'
        bank_dict[account_number] = [balance, password]
        return bank_dict, balance, password
                            




class Bank_Account:

    
    def __init__(self, account_number=0, balance = 100):
        self.account_number = account_number
        self.balance = balance


    def create_bank_account(self):
        #Ensure that bank account is 7 digits
        self.account_number = str((random.randint(1000000,9999999)))
        print ("Your new account number is: ")
        print (self.account_number)
        return self.account_number






def main():
    bank_dict = Bank.bank_database()
    trans_list = Bank.transactions()
    user_input = input ("Welcome to Bambank, do you already have an account? (Y/N): ")
    new_user = Bank_Account()

    #Checking ID against dict, or creating a new account and adding to dict
    if user_input == 'Y':
        account_number = input("Please enter your account ID: ")
        bank_balance = Bank.get_account_by_number(account_number, bank_dict)
        #print(bank_balance)       
    elif user_input == 'N':
        new_user.create_bank_account()
        account_number = new_user.account_number
        Bank.add_an_account(account_number, bank_dict)
    else:
        main()



    #Options for the user
    i= 0
    while i == 0:
        user_choice = input ("""What do you require to do:
                            Check Balance, press B.
                            Send Bambeuros,  press S.
                            Deposit, press D.
                            Check Transactions, press T.
                            Exit Service,  press E.
                            """)
        if user_choice == "B":
            bank_balance = Bank.check_balance(account_number, bank_dict)
            print(bank_balance)
        elif user_choice == "S":
            transfer_contact = int(input("What is the account ID to transfer to?: ")) 
            transfer_amount = int(input("How much do you want to transfer?: "))
            bank_balance = Bank.transfer(account_number, bank_dict, transfer_amount, transfer_contact, trans_list)
            #print (bank_dict)
            #Uncomment line above to check of both accounts beening updated
        elif user_choice == "D":
            deposit_amount = int(input("How much would you like to deposit?: "))
            Bank.deposit(deposit_amount, account_number, bank_dict, trans_list)
        elif user_choice == "T":
            print('\n'.join('{}: {}'.format(*k) for k in enumerate(trans_list)))
        elif user_choice == "E":
            print ("Thanks for using Bambank, goodbye!")
            i = i+1
        else:
            pass      



if __name__ == "__main__":
    main()
    
