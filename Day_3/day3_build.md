# Day 3 — Transaction List Engine (Lists + Loops + Conditions)

## What I built today

### 1. TransactionList class
Path: `finance_manager_app/backend/cli/transactions_list.py`

Features:
- Internal storage using a Python list: `_transactions`
- Methods:
  - `add_transaction(transaction)` → append a Transaction
  - `all()` → return a copy of all transactions
  - `total_amount()` → loop through all transactions and sum amounts
  - `filter_by_category(category)` → list comprehension filter
  - `filter_by_min_amount(min_amount)` → filter on amount >= value
  - `filter_by_date_range(start_date, end_date)` → inclusive date range filter

### 2. Test script
Path: `finance_manager_app/backend/cli/test_transactions_list.py`

What it does:
- Seeds 4 sample transactions (Food, Shopping, Food, Rent)
- Prints:
  - All transactions
  - Total amount
  - Only category = "Food"
  - Only transactions with amount >= 1000
  - Only transactions between `2025-12-01` and `2025-12-02`

## Sample output

```text
ALL TRANSACTIONS:
2025-12-01 | Food         | ₹500.00 | Lunch
2025-12-02 | Shopping     | ₹1500.00 | Clothes
2025-12-03 | Food         | ₹200.00 | Snacks
2025-12-01 | Rent         | ₹3000.00 | December rent

TOTAL AMOUNT:
5200.0

ONLY FOOD:
2025-12-01 | Food         | ₹500.00 | Lunch
2025-12-03 | Food         | ₹200.00 | Snacks

AMOUNT >= 1000:
2025-12-02 | Shopping     | ₹1500.00 | Clothes
2025-12-01 | Rent         | ₹3000.00 | December rent

DATE RANGE 2025-12-01 to 2025-12-02:
2025-12-01 | Food         | ₹500.00 | Lunch
2025-12-02 | Shopping     | ₹1500.00 | Clothes
2025-12-01 | Rent         | ₹3000.00 | December rent
