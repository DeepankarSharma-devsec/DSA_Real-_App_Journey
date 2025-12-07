# Python Standard Library Overview (My Notes)

---

## 1. Introduction

Python’s Standard Library is huge and super useful. It gives me ready‑made modules for math, randomness, dates, files, regex, and more. Knowing these saves time because I don’t need to reinvent everything.

---

## 2. `array` Module

Useful when I need a list‑like structure but with **one fixed data type** (more memory‑efficient than lists).

```python
import array

arr = array.array('i', [1, 2, 3, 4])  # 'i' = signed integer
print(arr)
```

---

## 3. `math` Module

Provides mathematical operations I’d otherwise code manually.

```python
import math

math.sqrt(16)  # 4.0
math.pi        # 3.14159...
```

---

## 4. `random` Module

Essential for simulations, games, ML experiments, sampling, etc.

```python
import random

random.randint(1, 10)
random.choice(['apple', 'banana', 'cherry'])
```

---

## 5. File and Directory Access

### A. `os` Module

Useful for navigating and manipulating directories.

```python
import os

os.getcwd()        # Current working directory
os.mkdir("test_dir")
```

### B. `shutil` Module

Higher‑level utilities like file copying.

```python
import shutil

shutil.copyfile("source.txt", "destination.txt")
```

---

## 6. `json` Module — Data Serialization

Perfect for APIs, config files, and web data.

```python
import json

data = {"name": "Krish", "age": 25}

# Convert dict → JSON string
json_str = json.dumps(data)

# Convert JSON string → dict
parsed = json.loads(json_str)
parsed["age"]
```

---

## 7. Handling CSV Files — `csv` Module

Super handy for Data Analysis workflows.

### Writing CSV

```python
import csv

with open("example.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Krish", 32])
```

### Reading CSV

```python
with open("example.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## 8. Dates and Times — `datetime`

Critical for logs, timestamps, ETL pipelines.

```python
from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
```

---

## 9. `time` Module

Simple time utilities like pausing execution.

```python
import time

print("Start")
time.sleep(2)  # pause for 2 seconds
print("End")
```

---

## 10. Regular Expressions — `re`

Great for pattern matching and data cleaning.

```python
import re

text = "There are 123 apples"
match = re.search(r"\d+", text)
if match:
    print(match.group())  # 123
```

---

## My Quick Takeaways

- Python’s standard library covers almost everything: math, file handling, time, regex, JSON, CSV.
- `os` + `shutil` = power combo for filesystem tasks.
- `re` is incredible for data cleanup and extraction.
- Once I master these modules, even basic scripts become super powerful.

