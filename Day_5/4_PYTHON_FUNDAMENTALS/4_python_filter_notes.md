# Python `filter()` Function — Personal Notes

## 1. Introduction

- `filter()` helps me pick **only the items** that satisfy a condition.
- It returns a **filter object** (iterator), so I usually convert it to a list.
- Perfect for data cleaning and extracting only the useful pieces of data.

---

## 2. Syntax

```python
filter(function, iterable)
```

- `function` → returns True/False  
- `iterable` → list, tuple, dictionary keys/values, etc.

---

## 3. Basic Usage (Using a Normal Function)

Filtering even numbers:

```python
def even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

even_nums = list(filter(even, numbers))
print(even_nums)
```

---

## 4. Using `filter()` with Lambda

Much cleaner for short logic.

```python
numbers = [1,2,3,4,5,6,7,8,9]

greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)
```

---

## 5. Multiple Conditions (Lambda + Logical Ops)

```python
numbers = [1,2,3,4,5,6,7,8,9]

filtered = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(filtered)
# [6, 8]
```

---

## 6. Filtering Dictionaries

Useful for real-world data like user profiles, products, API responses.

```python
people = [
    {'name': 'Krish', 'age': 32},
    {'name': 'Jack', 'age': 33},
    {'name': 'John', 'age': 25}
]

older_than_25 = list(filter(lambda p: p['age'] > 25, people))
print(older_than_25)
```

---

## Final Thoughts

- `filter()` is one of my go‑to tools for data preprocessing.
- Works beautifully with lambda → short, expressive, readable.
- Helps me keep only what I need, nothing more.

