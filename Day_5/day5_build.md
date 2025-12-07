# Day 5 — Query Engine (Functions, Lambda, Map, Filter)

## 1. Overview

Today I built the **Query Engine**, a functional-style querying layer that sits on top of the `TransactionList` module.  
It uses Python's functional programming features to perform clean, reusable, and powerful filtering and transformation operations.

Core concepts used today:

- Functions
- Lambda expressions
- map()
- filter()

This module forms the data-querying foundation for the Finance Manager App.

---

## 2. What I Built

### ✔ QueryEngine Class  
**Path:** `finance_manager_app/backend/cli/query_engine.py`

The `QueryEngine` connects directly to the `TransactionList` and provides high-level functions for:

- Category-based filtering  
- Month-based filtering  
- Amount range filtering  
- Extracting months or amounts from all transactions  

The logic is functional and modular, preparing the codebase for analytics, API integration, and frontend filtering later on.

---

## 3. Features Implemented

### 3.1 `filter_by_category(category)`
Returns all transactions with the given category.

```python
return list(filter(lambda t: t.category == category, self._all()))
```

### 3.2 `filter_by_month(month_str)`
Filters transactions matching a year-month prefix (YYYY-MM).

```python
return list(filter(lambda t: t.date.startswith(month_str), self._all()))
```

### 3.3 `filter_by_amount_range(min_amount, max_amount)`
Returns transactions where:
```
min_amount <= amount <= max_amount
```

```python
return list(
    filter(lambda t: min_amount <= t.amount <= max_amount, self._all())
)
```

### 3.4 `extract_months()`
Extracts the month portion from each transaction date.

```python
return list(map(lambda t: t.date[:7], self._all()))
```

### 3.5 `extract_amounts()`
Extracts all transaction amounts into a list.

```python
return list(map(lambda t: t.amount, self._all()))
```

---

## 4. Test Results

Executed via `test_query_engine.py`.

### ALL TRANSACTIONS
Correct list of all sample data printed.

### FILTER: CATEGORY = Food
Only the Food transactions were returned.

### FILTER: MONTH = 2025-12
All December 2025 transactions appeared (Food, Shopping, Salary).

### FILTER: AMOUNT RANGE 400 TO 2000
Correct transactions (₹500, ₹1500).

### EXTRACT MONTHS (map)
```text
['2025-12', '2025-12', '2025-12', '2025-11', '2025-12']
```

### EXTRACT AMOUNTS (map)
```text
[500.0, 1500.0, 200.0, 3000.0, 4500.0]
```

Everything behaved exactly as expected.

---

## 5. How Today's Learning Mapped to the Build

| Concept | Applied In | Example |
|--------|------------|---------|
| Functions | QueryEngine methods | `filter_by_amount_range()` |
| Lambda | Inline conditions | `lambda t: t.category == category` |
| map() | Data transformation | `extract_months()` |
| filter() | Conditional selection | `filter_by_category()` |

This is the first fully functional querying layer in the app.

---

## 6. Why Day 5 Matters

The Query Engine is now the **data-filtering brain** of the Finance Manager App.

It will directly power:

- API querying (Day 12+)
- Vue frontend filtering (Day 19+)
- Analytics (Day 26+)
- Sorting/searching algorithms (Day 30+)

This completes the foundation for smart data handling.

---

## 7. What’s Next (Day 6)

Next steps:

- Learn File I/O and working with JSON/CSV  
- Build a persistence layer  
- Implement saving + loading transactions  
- Turn the CLI system into a persistent personal finance tracker  

Day 6 transitions the app toward **real-world persistence**, not just in-memory logic.
