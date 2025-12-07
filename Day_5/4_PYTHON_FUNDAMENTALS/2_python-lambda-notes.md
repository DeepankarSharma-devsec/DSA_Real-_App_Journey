# Python Lambda Functions – My Personal Notes

### 1. What Exactly Is a Lambda Function?

- A **lambda function** is basically a *mini anonymous function*.
- No name, no full structure, just a quick one‑liner.
- I should use a lambda when:
  - The logic is short.
  - I don’t want to formally define a whole function using `def`.
  - I’m using it inside higher‑order functions like `map()` or `filter()`.

---

### 2. Lambda Syntax (Super Compact)

```python
lambda arguments: expression
```

Important reminders to myself:
- A lambda can take **multiple arguments**, but…
- It can only have **one expression** (no multiple lines, no loops directly inside).

---

### 3. `def` vs Lambda (Quick Comparison)

#### Normal Function

```python
def add(a, b):
    return a + b
```

#### Lambda Version

```python
addition = lambda a, b: a + b
print(addition(5, 6))
```

Both behave the same, but lambda avoids extra lines when the logic is simple.

---

### 4. Practical Lambda Examples

#### Checking Even Numbers

Standard way:

```python
def even(num):
    return num % 2 == 0
```

Lambda way:

```python
even1 = lambda num: num % 2 == 0
print(even1(12))  
```

#### Multiple Arguments Example

```python
addition_three = lambda x, y, z: x + y + z
print(addition_three(12, 13, 14))
```

---

### 5. Using Lambda with `map()` (Very Powerful!)

This is where lambda becomes extremely useful.

#### Task: Square every number in a list

Without lambda + map:
- I would create a loop.
- Square each number.
- Append to a new list.

With lambda + map:

```python
numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
```

Notes:
- `map()` returns a lazy map object.  
- I need `list()` to see the actual values.

---

### 6. Key Things I Want to Remember

1. Lambda = *anonymous, short, one‑expression function*.
2. Perfect for quick inline operations.
3. Best used with functions like `map()`, `filter()`, `sorted()`.
4. Not a replacement for normal functions, just a compact alternative.

These notes help me keep lambda usage clean and intentional instead of overusing it.

