import csv


def update_balance(update_account, file_users):
    rows = []
    headers = []

    with open(file_users, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        try:
            headers = next(reader)
        except StopIteration:
            return
        for row in reader:
            if len(row) < 4:
                continue
            if (
                row[0] == update_account.user_name
                and row[1] == update_account.bank_name
            ):
                row[2] = update_account.get_password()
                row[3] = update_account.balance
            rows.append(row)

        with open(file_users, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(headers)
            writer.writerows(rows)

    return update_balance
