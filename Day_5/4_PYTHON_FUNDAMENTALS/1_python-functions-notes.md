# Python Functions – My Personal Notes

### 1. Introduction to Functions

- A **function** is a reusable block of code that performs a single, well‑defined task.
- Why I should always use functions:
  - Keeps my code clean and organized.
  - Prevents repeating the same logic multiple times.
  - Makes debugging and future updates much easier.

---

### 2. Syntax & Structure

Basic function structure:

```python
def function_name(parameter1, parameter2):
    """Short description of what the function does"""
    # Code logic here
    return value
```

Key points I want to remember:
- `def` starts the function definition.
- Parameters are optional.
- Docstrings are not mandatory but extremely helpful.
- `return` is optional, but without it, the function gives back `None`.

---

### 3. Creating and Calling Functions

Example: Even/Odd Checker

```python
def check_even_odd(number):
    """Checks if a number is even or odd."""
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

check_even_odd(24)
```

Example: Function with return value

```python
def add(a, b):
    return a + b

result = add(2, 4)
print(result)
```

---

### 4. Function Parameters

#### A. Standard Parameters
Typical function parameters defined in the function signature.

#### B. Default Parameters

```python
def greet(name="Guest"):
    print(f"Hello {name}, Welcome!")

greet("Krish")
greet()
```

---

### 5. Variable Length Arguments (*args & **kwargs)

Sometimes I don’t know how many inputs I will receive. These help manage that.

#### A. *args – Positional Arguments

- Collects all extra positional args into a **tuple**.

```python
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, "Krish")
```

#### B. **kwargs – Keyword Arguments

- Collects keyword arguments into a **dictionary**.

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krish", age=32, country="India")
```

#### C. Combining *args and **kwargs

```python
def combined_example(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

combined_example(1, 2, 3, name="Krish", age=32)
```

Important rule: *args must come **before** **kwargs.

---

### 6. Return Statement

- `return` immediately ends the function.
- Functions can return multiple values (Python packs them into a tuple).

```python
def multiply(a, b):
    product = a * b
    return product, a

result, original_a = multiply(2, 3)
print(result)
print(original_a)
```

---

### Summary (My Quick Revision)

- Use functions to avoid repeating logic.
- Default arguments make functions flexible.
- `*args` handles unlimited positional inputs.
- `**kwargs` handles unlimited keyword inputs.
- Always remember: first `*args`, then `**kwargs`.
- Functions can return multiple values as tuples.

