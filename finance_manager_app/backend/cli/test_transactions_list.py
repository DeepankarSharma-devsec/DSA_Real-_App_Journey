from transaction import Transaction
from transactions_list import TransactionList


def seed_data() -> TransactionList:
    t_list = TransactionList()

    t_list.add_transaction(Transaction(500, "Food", "2025-12-01", "Lunch"))
    t_list.add_transaction(Transaction(1500, "Shopping", "2025-12-02", "Clothes"))
    t_list.add_transaction(Transaction(200, "Food", "2025-12-03", "Snacks"))
    t_list.add_transaction(Transaction(3000, "Rent", "2025-12-01", "December rent"))

    return t_list


if __name__ == "__main__":
    t_list = seed_data()

    print("ALL TRANSACTIONS:")
    for t in t_list.all():
        print(t)
    print()

    print("TOTAL AMOUNT:")
    print(t_list.total_amount())
    print()

    print("ONLY FOOD:")
    for t in t_list.filter_by_category("Food"):
        print(t)
    print()

    print("AMOUNT >= 1000:")
    for t in t_list.filter_by_min_amount(1000):
        print(t)
    print()

    print("DATE RANGE 2025-12-01 to 2025-12-02:")
    for t in t_list.filter_by_date_range("2025-12-01", "2025-12-02"):
        print(t)
