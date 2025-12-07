# Python Modules and Packages (My Notes)

---

## 1. Introduction

- Modules and packages help me **organize**, **reuse**, and **structure** my code neatly.
- Instead of rewriting functions, I can import built‑in or custom modules.
- Packages allow grouping multiple modules together.

---

## 2. Using Built‑in Modules

### Importing the entire module

```python
import math
math.sqrt(16)  # 4.0
```

### Importing specific functions

```python
from math import sqrt, pi
sqrt(25)  # 5.0
pi       # 3.14159...
```

### Importing everything

```python
from math import *
sqrt(16)
```

---

## Installing External Packages (e.g., NumPy)

1. Add `numpy` to **requirements.txt**
2. Install using:

```bash
pip install numpy
# or
pip install -r requirements.txt
```

3. Use an alias:

```python
import numpy as np
arr = np.array([1, 2, 3])
```

---

## 3. Creating My Own Packages

A package is simply a **folder** with an `__init__.py` file.

### Example folder structure

```
package/
├── __init__.py
├── maths.py
└── subpackages/
    ├── __init__.py
    └── mult.py
```

### Sample module: maths.py

```python
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b
```

### Importing my custom modules

#### Import a specific function

```python
from package.maths import addition
addition(2, 3)
```

#### Import the whole module

```python
from package import maths
maths.addition(2, 3)
```

#### Import everything

```python
from package.maths import *
addition(2, 3)
subtraction(4, 3)
```

---

## 4. Subpackages

Inside `subpackages/mult.py`:

```python
def multiply(a, b):
    return a * b
```

### Importing functions from subpackages

```python
from package.subpackages.mult import multiply
multiply(4, 5)  # 20
```

---

## Summary Table

| Action | Syntax |
|-------|--------|
| Import module | `import module_name` |
| Import with alias | `import module_name as alias` |
| Import specific function | `from module_name import function` |
| Install package | `pip install package_name` |
| Make a folder a package | Add `__init__.py` |

---

## My Quick Takeaways

- `__init__.py` is what turns a folder into a **package**.
- Use `from module import function` when I only need specific pieces.
- Packages help keep big projects clean and modular.
- Always maintain a `requirements.txt` so reinstalling dependencies is easy.

