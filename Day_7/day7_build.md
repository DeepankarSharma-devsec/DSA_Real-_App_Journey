# Day 7 — TransactionService (Exceptions + OOP Service Layer)

## 1. Overview

Today I added a proper **service layer** to my Finance Manager app: `TransactionService`.

This layer is responsible for:

- Validating all transaction inputs (amount, category, date)
- Raising clear, custom exceptions on invalid data
- Only adding valid `Transaction` objects into `TransactionList`

It applies everything I learned about:

- Exception handling (`try/except`, custom exceptions)
- OOP (classes, encapsulation, abstraction, inheritance, polymorphism)

---

## 2. What I Built

### ✔ `transaction_service.py`
**Path:** `finance_manager_app/backend/cli/transaction_service.py`

### Custom Exceptions

- `TransactionError` → base class for all transaction-related errors
- `InvalidAmountError` → raised when amount is non-numeric or <= 0
- `InvalidCategoryError` → raised when category is empty or not registered in `CategoryEngine`
- `InvalidDateError` → raised when date is missing or not in `YYYY-MM-DD` format

These classes make error handling more explicit and readable.

### TransactionService Class

The `TransactionService` acts as a façade around core components:

- `TransactionList`
- `CategoryEngine`
- `Transaction`

It exposes two main methods:

1. `create_transaction(amount, category, date=None, note="")`
2. `safe_create_transaction(amount, category, date=None, note="")`

---

## 3. Validation Logic

### `_validate_amount(amount)`

- Converts the input to `float`
- Raises `InvalidAmountError` if:
  - Conversion fails (non-numeric input)
  - Value <= 0

### `_validate_category(category)`

- Strips whitespace
- Ensures it’s not empty
- Calls `CategoryEngine.exists()` to ensure the category is registered
- Raises `InvalidCategoryError` if invalid

### `_validate_date(date_str)`

- If `None` → uses today’s date in `YYYY-MM-DD` format
- Else:
  - Uses `datetime.strptime()` to validate `YYYY-MM-DD`
  - Normalizes format via `strftime`
- Raises `InvalidDateError` if parsing fails

These methods are kept **internal** (`_validate_*`) to enforce encapsulation and hide implementation details.

---

## 4. Public API Methods

### `create_transaction(...)`

Steps:

1. Validate amount, category, and date using internal helpers.
2. Create a `Transaction` instance with the validated values.
3. Add the transaction to the `TransactionList`.
4. Return the created transaction.

Raises:

- `InvalidAmountError`
- `InvalidCategoryError`
- `InvalidDateError`

### `safe_create_transaction(...)`

- Wraps `create_transaction` in a `try/except TransactionError` block.
- On error:
  - Prints a friendly log message.
  - Returns `None` instead of raising, so callers can fail gracefully.

This is a real example of using exceptions in production-style code.

---

## 5. Test Script & Results

### `test_transaction_service.py`
**Path:** `finance_manager_app/backend/cli/test_transaction_service.py`

What it tests:

1. **Success case**  
   - Creates a valid transaction: amount 500, category "Food", date "2025-12-01".
   - Confirms it’s added to `TransactionList`.

2. **Invalid amount**  
   - Tries `-100` as amount.  
   - Catches `InvalidAmountError`.

3. **Invalid category**  
   - Uses `"Random"` which is not in `CategoryEngine`.  
   - Catches `InvalidCategoryError`.

4. **Invalid date**  
   - Uses `"12-01-2025"` instead of `"2025-12-01"`.  
   - Catches `InvalidDateError`.

5. **Safe mode**  
   - Calls `safe_create_transaction` with an unknown category.  
   - Service prints an error message.
   - Function returns `None`.  

### Sample Output (Summary)

- One valid transaction created and printed.
- Clear error messages:
  - `Amount must be greater than zero.`
  - `Unknown category: Random`
  - `Date must be in 'YYYY-MM-DD' format.`
- `safe_create_transaction` logs:
  - `[TransactionService] Failed to create transaction: Unknown category: UnknownCategory`
- Final transaction count: `1`.

---

## 6. How Day 7 Learning Mapped to the Build

- **Exception Handling** → custom exceptions, `try/except`, safe wrapper.
- **OOP Basics** → `TransactionService` as a separate, responsible class.
- **Inheritance** → custom exceptions inheriting from `TransactionError` / `Exception`.
- **Polymorphism** → different exception subclasses can all be caught as `TransactionError`.
- **Encapsulation** → `_validate_*` methods hide internal rules.
- **Abstraction** → callers only see `create_transaction` / `safe_create_transaction`, not individual validation details.

---

## 7. Why Day 7 Matters

Before today:

- Any part of the code could directly construct a `Transaction`.
- There was no central place for validation & error handling.

After today:

- All transaction creation can be routed through `TransactionService`.
- The app gains a **single source of truth** for:
  - Amount validation
  - Category validation
  - Date validation
- It becomes much safer to accept input from:
  - Future CLI prompts
  - Flask API forms
  - Vue frontend

This is a real step toward **clean architecture and production-ready behavior**.

---

## 8. Next Steps (Day 8+)

- Add structured logging or error reporting.
- Start wiring CLI or simple menu interface that uses `TransactionService`.
- Begin preparing for Flask integration by reusing service and query layers.
