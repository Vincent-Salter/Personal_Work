class Bank_accounts:

    def __init__(self):
        self.is_active = True

    def account_setup(self, customer_name_input, customer_email_input, customer_address_input, account_number_input, account_balance_input, overdraft_limit_input):
        self.customer_name = customer_name_input
        self.customer_email = customer_email_input
        self.customer_address = customer_address_input
        self.account_number = account_number_input
        self.account_balance = account_balance_input
        self.overdraft_limit = overdraft_limit_input

    def deposit(self, money_in):
        self.account_balance += money_in

    def withdraw(self, money_out):
        if self.account_balance - money_out < -self.overdraft_limit:
            print("Insufficient funds. Cannot withdraw beyond overdraft limit.")
        else:
            self.account_balance -= money_out
        
    def transfer_funds(self, transfer_money, destination):
        self.account_balance -= transfer_money
        destination += transfer_money     
        

    def update_personal_information(self, new_customer_name, new_customer_email, new_customer_address):
        self.customer_address = new_customer_address
        self.customer_email = new_customer_email
        self.customer_name = new_customer_name

    def closing_an_account(self):
        if self.account_balance > 0:
            print("Account has a balance. Please withdraw all fund before closing.")
            return
        if self.account_balance < 0:
            print("Account has an overdraft. Please deposit funds before closing.")
            return
        self.is_active = False

    def display_user_information(self):
        pass

    def interest_calculator(self):
        pass

# Question for mother about init(self) being the only needed parameter and we can just have self in the body of the method
transfer_money = float(input("Transfer funds: "))

viinny = Bank_accounts()