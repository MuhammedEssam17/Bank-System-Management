import csv
from Bank_Account import Bank_Account


def login(file_users, user_name, bank_name, password):

    with open(file_users, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        try:
            next(reader)
        except StopIteration:
            return None
        for row in reader:
            if len(row) < 4:
                continue
            if row[0] == user_name and row[1] == bank_name:
                accounts = Bank_Account(row[0], row[1], row[2], row[3], file_users)
                if accounts.check_password(password):
                    return accounts
    return None
