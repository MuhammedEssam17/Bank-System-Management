import csv


def delete_account(remove, file_users):
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
            if row[0] == remove.user_name and row[1] == remove.bank_name:
                continue
            rows.append(row)

        with open(file_users, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(headers)
            writer.writerows(rows)
    return delete_account
