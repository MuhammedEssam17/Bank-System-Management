import csv


def create_account(user_name, bank_name, password, balance, file_users):
    with open(file_users, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow([user_name, bank_name, password, balance])
        print(
            f"Your account has been created successfully, Welcome {user_name} to {bank_name} Bank\n"
        )
