import os
from transaction import Transaction
from transactions_list import TransactionList
from file_store import save_transactions_to_json, load_transactions_from_json


def seed_data() -> TransactionList:
    t_list = TransactionList()
    t_list.add_transaction(Transaction(500, "Food", "2025-12-01", "Lunch"))
    t_list.add_transaction(Transaction(1500, "Shopping", "2025-12-02", "Clothes"))
    t_list.add_transaction(Transaction(200, "Food", "2025-12-03", "Snacks"))
    t_list.add_transaction(Transaction(3000, "Rent", "2025-12-01", "December rent"))
    return t_list


def print_section(title: str) -> None:
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


if __name__ == "__main__":
    json_path = "finance_manager_app/backend/cli/data/transactions_day6.json"

    # 1. Seed data
    original_list = seed_data()

    print_section("ORIGINAL TRANSACTIONS")
    for t in original_list.all():
        print(t)

    # 2. Save to JSON
    print_section(f"SAVING TO JSON: {json_path}")
    save_transactions_to_json(original_list, json_path)
    print("File exists after save?", os.path.exists(json_path))

    # 3. Load from JSON
    print_section("LOADING FROM JSON")
    loaded_list = load_transactions_from_json(json_path)
    for t in loaded_list.all():
        print(t)

    # 4. Simple verification: count + total amount
    print_section("VERIFICATION")
    print("Original count:", len(original_list.all()))
    print("Loaded count  :", len(loaded_list.all()))
    print("Original total:", original_list.total_amount())
    print("Loaded total  :", loaded_list.total_amount())
