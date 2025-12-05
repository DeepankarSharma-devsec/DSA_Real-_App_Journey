# Python Data Structures: Dictionaries (My Notes)

### 1. Introduction

- **Dictionaries** store data as **key–value pairs**.
- Keys must be **unique** and **immutable** (string, int, tuple).
- Values can be **any type** and can repeat.
- Dictionaries are **mutable**, meaning I can add, update, or delete entries anytime.

---

### 2. Creating Dictionaries

```python
empty_dict = {}
empty_dict = dict()
```

Populated dictionary example:

```python
student = {
    "name": "Krish",
    "age": 32,
    "grade": "A"
}
```

> Reminder to myself: If duplicate keys are used, Python keeps only the **last** value.

---

### 3. Accessing Values

**Direct key access:**

```python
student["grade"]
```

**Safer access using `.get()`** (avoids errors):

```python
student.get("grade")
student.get("last_name", "Not Available")
```

---

### 4. Updating & Modifying Dictionaries

- **Add new key:**

```python
student["address"] = "India"
```

- **Update value:**

```python
student["age"] = 33
```

- **Delete a key:**

```python
del student["grade"]
```

---

### 5. Useful Dictionary Methods

```python
student.keys()
student.values()
student.items()
```

`items()` is especially useful when looping because it gives `(key, value)` pairs.

---

### 6. Copying Dictionaries (Important!)

Accidental referencing can cause bugs.

**Bad:**

```python
dict2 = dict1  # both point to same memory
```

**Correct shallow copy:**

```python
dict2 = dict1.copy()
```

---

### 7. Looping Through Dictionaries

**Iterate keys:**

```python
for key in student.keys():
    print(key)
```

**Iterate values:**

```python
for value in student.values():
    print(value)
```

**Iterate key–value pairs:**

```python
for key, value in student.items():
    print(key, value)
```

---

### 8. Nested Dictionaries

Example:

```python
students = {
    "student1": {"name": "Krish", "age": 32},
    "student2": {"name": "Peter", "age": 35}
}
```

Access nested values:

```python
students["student2"]["name"]
```

---

### 9. Dictionary Comprehension

My favourite shortcut!

```python
squares = {x: x**2 for x in range(5)}
```

Conditional version:

```python
evens = {x: x**2 for x in range(10) if x % 2 == 0}
```

---

### 10. Practical Use Cases

#### A. Frequency Counter

```python
numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
```

#### B. Merging Dictionaries Using `**`

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = {**dict1, **dict2}
```

> Note: When keys overlap, values from the right dictionary win.

---

### Summary (My Quick Recall)

- Use `{}` for dictionaries.
- Keys must be unique; values can repeat.
- `.get()` is safer than `[]`.
- `.items()` is the best way to loop.
- `.copy()` prevents accidental reference issues.
- Dictionary comprehension makes creation super clean.

