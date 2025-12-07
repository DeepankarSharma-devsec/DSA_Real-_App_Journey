# Python File Operations (My Notes)

---

## 1. Introduction

Python makes file handling super easy. I can create, read, write, append, and even work with binary files using just a few built-in functions. This is essential for logs, configs, ETL pipelines, and general automation.

---

## 2. Opening Files with `open()`

Always better to use `with open(...)` because it auto‑closes the file.

**Common modes I need to remember:**

- `'r'` → read (error if file doesn't exist)
- `'w'` → write (overwrites the entire file)
- `'a'` → append
- `'r+'` → read + write
- `'w+'` → write + read (also overwrites)
- `'b'` → binary mode (`'rb'`, `'wb'`)

```python
with open("example.txt", "r") as f:
    content = f.read()
```

---

## 3. Reading Files

### A. Read whole file:

```python
with open("example.txt", "r") as f:
    content = f.read()
```

### B. Read line by line:

```python
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## 4. Writing to Files

### A. Write (overwrites):

```python
with open("example.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Another line")
```

### B. Append:

```python
with open("example.txt", "a") as f:
    f.write("\nAppending new line")
```

### C. Write multiple lines:

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "a") as f:
    f.writelines(lines)
```

---

## 5. Working with Binary Files

### Write binary:

```python
with open("example.bin", "wb") as f:
    f.write(b"Hello World")
```

### Read binary:

```python
with open("example.bin", "rb") as f:
    data = f.read()
    print(data)
```

---

## 6. `w+` Mode and Cursor Control (`seek`)

`w+` lets me write and then read. But I must move the cursor back to the start.

```python
with open("example.txt", "w+") as f:
    f.write("Hello World")
    f.seek(0)        # rewind cursor
    print(f.read())
```

---

## 7. Practical Examples

### Copy a file:

```python
with open("source.txt", "r") as src:
    content = src.read()

with open("dest.txt", "w") as dest:
    dest.write(content)
```

### Assignment Logic (File Statistics):

- **Lines:** `len(f.readlines())`
- **Words:** loop + `line.split()`
- **Characters:** `len(content)`

---

## Final Thoughts

File handling is one of the most powerful parts of Python. Once I combine these skills with loops, lists, dictionaries, and regex, I can automate almost anything—from log parsing to report generation.

