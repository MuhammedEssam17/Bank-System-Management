from Update_acc import update_balance
from Create_acc import create_account
from Delete import delete_account


class Bank_System:
    def __init__(self, file_users="Names.csv"):
        self.file_users = file_users

    def create_account(self, user_name, bank_name, password, balance):
        return create_account(user_name, bank_name, password, balance, self.file_users)

    def login(self, user_name, bank_name, password):
        import auth

        return auth.login(self.file_users, user_name, bank_name, password)

    def update_balance(self, update_account):
        update_balance(update_account, self.file_users)

    def delete_account(self, remove):
        return delete_account(remove, self.file_users)
