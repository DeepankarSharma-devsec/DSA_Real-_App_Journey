from transaction import Transaction
from transactions_list import TransactionList
from query_engine import QueryEngine


def seed_data() -> TransactionList:
    t_list = TransactionList()

    t_list.add_transaction(Transaction(500, "Food", "2025-12-01", "Lunch"))
    t_list.add_transaction(Transaction(1500, "Shopping", "2025-12-02", "Clothes"))
    t_list.add_transaction(Transaction(200, "Food", "2025-12-03", "Snacks"))
    t_list.add_transaction(Transaction(3000, "Rent", "2025-11-30", "November rent"))
    t_list.add_transaction(Transaction(4500, "Salary", "2025-12-01", "Monthly salary"))

    return t_list


def print_section(title: str) -> None:
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


if __name__ == "__main__":
    t_list = seed_data()
    engine = QueryEngine(t_list)

    print_section("ALL TRANSACTIONS")
    for t in t_list.all():
        print(t)

    print_section("FILTER: CATEGORY = Food")
    for t in engine.filter_by_category("Food"):
        print(t)

    print_section("FILTER: MONTH = 2025-12")
    for t in engine.filter_by_month("2025-12"):
        print(t)

    print_section("FILTER: AMOUNT RANGE 400 TO 2000")
    for t in engine.filter_by_amount_range(400, 2000):
        print(t)

    print_section("EXTRACT MONTHS (map)")
    print(engine.extract_months())

    print_section("EXTRACT AMOUNTS (map)")
    print(engine.extract_amounts())

