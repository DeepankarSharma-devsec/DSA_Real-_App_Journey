from transactions_list import TransactionList
from category_engine import CategoryEngine
from transaction_service import (
    TransactionService,
    InvalidAmountError,
    InvalidCategoryError,
    InvalidDateError,
)


def print_section(title: str) -> None:
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


def setup_service() -> TransactionService:
    t_list = TransactionList()
    cat_engine = CategoryEngine()
    service = TransactionService(t_list, cat_engine)
    return service


if __name__ == "__main__":
    service = setup_service()
    t_list = service._t_list   # just for inspection/printing

    # 1. SUCCESS CASE
    print_section("SUCCESS: VALID TRANSACTION")
    tx = service.create_transaction(500, "Food", "2025-12-01", "Lunch")
    print("Created:", tx)
    print("Total transactions:", len(t_list.all()))

    # 2. INVALID AMOUNT (negative)
    print_section("ERROR: INVALID AMOUNT (-100)")
    try:
        service.create_transaction(-100, "Food", "2025-12-01", "Invalid amount test")
    except InvalidAmountError as e:
        print("Caught InvalidAmountError:", e)

    # 3. INVALID CATEGORY (not in CategoryEngine)
    print_section("ERROR: INVALID CATEGORY ('Random')")
    try:
        service.create_transaction(300, "Random", "2025-12-01", "Invalid category test")
    except InvalidCategoryError as e:
        print("Caught InvalidCategoryError:", e)

    # 4. INVALID DATE (wrong format)
    print_section("ERROR: INVALID DATE ('12-01-2025')")
    try:
        service.create_transaction(300, "Food", "12-01-2025", "Invalid date test")
    except InvalidDateError as e:
        print("Caught InvalidDateError:", e)

    # 5. SAFE MODE: safe_create_transaction (no crash, returns None)
    print_section("SAFE CREATE: INVALID CATEGORY USING safe_create_transaction")
    tx_safe = service.safe_create_transaction(400, "UnknownCategory", "2025-12-01", "Safe mode")
    print("Result of safe_create_transaction:", tx_safe)
    print("Total transactions after all tests:", len(t_list.all()))
