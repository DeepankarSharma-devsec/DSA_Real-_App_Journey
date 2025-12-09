# Day 6 — Persistence Layer (Modules, Stdlib, File I/O, Paths)

## 1. Overview

Today I turned my Finance Manager app from an in-memory prototype into a **persistent system** by adding a JSON-based storage layer.

I used what I learned about:

- Importing modules and packages
- Python standard library (json, os)
- File operations (open, read, write)
- File paths and directory handling

to build a clean, reusable `file_store.py` module.

---

## 2. What I Built

### ✔ `file_store.py`
**Path:** `finance_manager_app/backend/cli/file_store.py`

This module is responsible for saving and loading all transactions using a JSON file.

It exposes two main functions:

1. `save_transactions_to_json(t_list, filepath)`
2. `load_transactions_from_json(filepath) -> TransactionList`

It acts as the persistence layer for the CLI part of my Finance Manager app.

---

## 3. Features Implemented

### 3.1 `save_transactions_to_json(t_list, filepath)`

- Accepts a `TransactionList` and a file path.
- Ensures the parent directory exists (creates it if missing).
- Converts each `Transaction` object to a dictionary via `.to_dict()`.
- Writes the list of dicts to a JSON file with:

  ```python
  json.dump(data, f, ensure_ascii=False, indent=2)
