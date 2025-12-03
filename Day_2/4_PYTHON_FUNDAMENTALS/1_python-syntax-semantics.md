# Personal Notes: Python Syntax and Semantics

------------------------------------------------------------------------

## 1. What Syntax and Semantics Mean (My Understanding)

### ✔️ Syntax

Syntax is basically the **grammar** of Python.\
If something is structured wrong, Python stops the program before
running it and raises a **SyntaxError**.

### ✔️ Semantics

Semantics = the **meaning** or behavior of the code.\
Even when syntax is correct, the logic may still be wrong.

------------------------------------------------------------------------

## 2. Comments in Python (How I Document My Code)

### ✔️ Single-Line Comments (`#`)

``` python
# This is a single line comment
print("Hello World")
```

### ✔️ Multi-Line Comments (Triple Quotes)

``` python
\"\"\"\nThis is a\nmulti-line\ncomment\n\"\"\"
```

------------------------------------------------------------------------

## 3. Basic Syntax Rules I Must Remember

### ✔️ Case Sensitivity

``` python
name = "Chris"
Name = "Nick"
```

### ✔️ Indentation Defines Code Blocks

``` python
age = 32
if age > 30:
    print(age)
print("Done")
```

### ✔️ Line Continuation (`\`)

``` python
total = 1 + 2 + 3 + \
        4 + 5 + 6
```

### ✔️ Multiple Statements on One Line (`;`)

``` python
x = 5; y = 10; print(x + y)
```

------------------------------------------------------------------------

## 4. Semantics in Python (Runtime Behavior)

### ✔️ Dynamic Typing

``` python
age = 32
name = "Chris"
```

### ✔️ Dynamic Reassignment

``` python
var = 10
var = "Chris"
```

------------------------------------------------------------------------

## 5. Common Errors

### ❌ IndentationError

Occurs when spacing is inconsistent.

### ❌ NameError

``` python
a = b  # b is not defined
```

------------------------------------------------------------------------

## 6. Indentation Example

``` python
if True:
    print("Correct Indentation")
    if False:
        print("This won't print")
    print("This will print")
print("Outside the if block")
```

------------------------------------------------------------------------

These notes help me clearly distinguish how Python behaves syntactically
and semantically.
