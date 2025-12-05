# Day 4 — Category Engine (Sets + Tuples + Dictionaries)

## What I built today

### ✔ CategoryEngine class
Path: `finance_manager_app/backend/cli/category_engine.py`

The Category Engine manages all categories in the Finance Manager App using:

- **Tuple** for DEFAULT_CATEGORIES (immutable baseline)  
- **Dictionary** for category metadata  
- **Set** for uniqueness and fast membership checks  

### ✔ Features implemented
- Auto-load default categories from a tuple
- Add new categories (`add_category`)
- Remove categories (`remove_category`)
- Check if a category exists (`exists`)
- List all categories (sorted)
- Get metadata for a category (`get_category_info`)
- List categories by type: expense / income (`list_by_type`)

### ✔ Internal Data Structures

#### 1. DEFAULT_CATEGORIES (tuple)
```python
DEFAULT_CATEGORIES = (
    ("Food", "expense", 8000),
    ("Rent", "expense", 15000),
    ("Shopping", "expense", 5000),
    ("Transport", "expense", 3000),
    ("Entertainment", "expense", 4000),
    ("Health", "expense", 2000),
    ("Salary", "income", None),
)
