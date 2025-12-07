# Advanced File Path Operations (`os` Module) — My Notes

---

## 1. Introduction

These notes are my quick reference for handling files, folders, and paths using Python’s `os` module. This is super important when I start building automation scripts, ETL pipelines, or any project that needs to read/write files reliably across platforms.

---

## 2. Directory Operations

### ✅ Creating a New Directory

```python
import os

new_directory = "package"
os.mkdir(new_directory)
print(f"Directory '{new_directory}' created")
```

### ✅ Listing Files and Directories

```python
items = os.listdir('.')
print(items)
# Example: ['example.bin', 'destination.txt', 'package']
```

---

## 3. Path Joining with `os.path.join`

This is one of the most important things. It helps avoid broken paths when switching between Windows (`\`) and Linux/Mac (`/`).

```python
import os

dir_name = "folder"
file_name = "file.txt"

full_path = os.path.join(dir_name, file_name)
print(full_path)
# Windows → folder\file.txt
# Linux/Mac → folder/file.txt
```

---

## 4. Checking Existence with `os.path.exists`

Before deleting, reading, or writing, I should always check existence.

```python
import os

path = "example1.txt"

if os.path.exists(path):
    print(f"'{path}' exists")
else:
    print(f"'{path}' does not exist")
```

---

## 5. Checking if Path is File or Directory

```python
import os

path = "example.txt"

if os.path.isfile(path):
    print("It’s a file")
elif os.path.isdir(path):
    print("It’s a directory")
else:
    print("It’s neither")
```

---

## 6. Relative vs Absolute Paths

### Convert relative → absolute

```python
import os

relative_path = "example.txt"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)
```

---

## Summary Table

| Function | What It Does |
|---------|---------------|
| `os.mkdir(path)` | Creates a directory |
| `os.listdir(path)` | Lists files & folders |
| `os.path.join(a, b)` | Joins path pieces safely |
| `os.path.exists(path)` | Checks if a path exists |
| `os.path.isfile(path)` | Checks if path is a file |
| `os.path.isdir(path)` | Checks if path is a directory |
| `os.path.abspath(path)` | Converts to absolute path |

---

These are core tools I’ll reuse constantly, especially when working on real Python projects that handle multiple files.
