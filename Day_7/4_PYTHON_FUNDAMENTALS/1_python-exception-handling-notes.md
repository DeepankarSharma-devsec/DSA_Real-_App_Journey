# Python Exception Handling (My Personal Notes)

### 1. Introduction

Exception Handling helps me prevent programs from crashing and lets me show clean error messages instead of raw stack traces.

I remind myself:

- **Errors** break the normal flow.
- **Exceptions** are events raised during execution.
- I can *catch* and handle them.

Common exceptions I keep running into:

- `ZeroDivisionError`
- `FileNotFoundError`
- `ValueError`
- `TypeError`
- `NameError`

---

### 2. Basic Structure: `try` + `except`

This is the core pattern.

```python
try:
    a = b   # b is not defined
except NameError as ex:
    print("Variable not defined.")
    print(ex)
```

Another classic case:

```python
try:
    result = 1 / 0
except ZeroDivisionError as ex:
    print("Cannot divide by zero.")
    print(ex)
```

---

### 3. Multiple Exceptions (Specific → Generic)

I always place specific exceptions first, then the generic `Exception`.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Division by zero.")

except Exception as ex:
    print(f"Unexpected error: {ex}")
```

---

### 4. `else` Block (Runs Only When No Error)

I use it for logic that should execute only when the `try` succeeded.

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Zero not allowed.")
else:
    print("Result:", result)
```

---

### 5. `finally` Block (Always Runs)

Great for cleanup tasks.

```python
try:
    num = int(input())
    result = 10 / num
except ZeroDivisionError:
    print("Invalid division.")
else:
    print(result)
finally:
    print("This runs no matter what.")
```

---

### 6. Practical Example: File Handling with Safe Cleanup

This is a real‑world pattern I use often.

```python
try:
    file = open("example1.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

except Exception as ex:
    print(f"Error: {ex}")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")
```

The `locals()` check avoids an error if opening failed.

---

### Summary Table

| Keyword | My Interpretation |
|--------|-------------------|
| **try** | Code that might fail. |
| **except** | What I want to do if it fails. |
| **else** | Runs only when no exception occurred. |
| **finally** | Runs regardless of success or failure (cleanup). |

---

These exception‑handling patterns show up everywhere in real projects, especially when dealing with files, user input, database connections, and network operations.
