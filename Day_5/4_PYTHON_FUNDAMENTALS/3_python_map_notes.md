# Python `map()` Function — Personal Notes

## 1. Introduction

- The `map()` function lets me apply a function to **every item** in an iterable.
- It returns a **map object** (an iterator), so I usually convert it to a list.
- Super useful for transforming data without writing manual loops.

---

## 2. Syntax

```python
map(function, iterable)
```

- `function`: what I want applied to each item.
- `iterable`: list, tuple, string, etc.

---

## 3. Basic Usage

### Squaring numbers (classic example)

```python
def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(square, numbers))
print(result)
# [1, 4, 9, 16, 25, 36, 49, 64]
```

---

## 4. Using `map()` with Lambda Functions

I love using lambda inside `map()` for quick, small transformations.

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x * x, numbers))
print(squared)
```

---

## 5. Mapping Multiple Iterables

`map()` can take multiple lists, but then the function must accept the same number of arguments.

Example: adding list items index‑wise:

```python
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

added = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added)
# [5, 7, 9]
```

---

## 6. Practical Use‑Cases

### A. Converting Data Types

```python
str_numbers = ["1", "2", "3", "4"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)
```

---

### B. String Manipulation

```python
words = ["apple", "banana", "cherry"]
upper_words = list(map(str.upper, words))
print(upper_words)
```

---

### C. Extracting Data from List of Dictionaries

```python
people = [
    {"name": "Krish", "age": 32},
    {"name": "Jack", "age": 33}
]

names = list(map(lambda p: p["name"], people))
print(names)
```

---

## Final Thoughts

- `map()` = clean, readable transformations.
- Pairs beautifully with `lambda`.
- Saves me from writing repetitive loops.
