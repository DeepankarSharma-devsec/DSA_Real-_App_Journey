# Personal Notes: Python Variables

------------------------------------------------------------------------

## 1. What Variables Are (My Understanding)

Variables are just **names that store data**.\
In Python, they come into existence the moment I assign something to
them --- no need for declarations like `int a`.

Example:

``` python
a = 100
```

Python automatically creates the variable and manages memory for it.

------------------------------------------------------------------------

## 2. Assigning Variables

Different data types can be assigned easily:

``` python
age = 32          # int
height = 6.1      # float
name = "Krish"    # str
is_student = True # bool
```

To print values:

``` python
print("Age:", age)
print("Name:", name)
```

------------------------------------------------------------------------

## 3. Naming Variables (Rules I Must Follow)

### ✔️ Rules

1.  Must start with a **letter** or **underscore**
2.  Can contain letters, numbers, underscores\
3.  **Cannot start with a number**
4.  Python is **case-sensitive**
5.  Use descriptive names (`first_name` instead of `fn`)

### ✔️ Valid vs Invalid

  Status   Variable       Why
  -------- -------------- ---------------------------------
  ✅       `first_name`   Starts with letter
  ✅       `_age`         Starts with underscore
  ✅       `name1`        Number allowed but not at start
  ❌       `1age`         Starts with number
  ❌       `first-name`   Hyphen not allowed
  ❌       `@name`        Special characters not allowed

------------------------------------------------------------------------

## 4. Python Data Types (How Python Interprets Variables)

Python determines the variable type **at runtime**.

Common types:

-   `int`
-   `float`
-   `str`
-   `bool`

To check a variable type:

``` python
age = 25
print(type(age))
```

------------------------------------------------------------------------

## 5. Type Conversion (Casting)

### ✔️ Integer → String

``` python
age = 25
age_str = str(age)
```

### ✔️ String → Integer

``` python
num_str = "25"
num_int = int(num_str)
```

> Note: `"Krish"` cannot be converted into an integer.

### ✔️ Float → Integer (Truncates)

``` python
height = 6.1
height_int = int(height)  # 6
```

### ✔️ Integer → Float

``` python
num = 5
num_float = float(num)  # 5.0
```

------------------------------------------------------------------------

## 6. Dynamic Typing (Python's Flexibility)

Variables can change types as the program runs.

``` python
var = 10
print(type(var))

var = "Hello"
print(type(var))

var = 3.14
print(type(var))
```

------------------------------------------------------------------------

## 7. Input Function

`input()` **always returns a string**.

``` python
name = input("Enter name: ")
age = int(input("Enter age: "))  # Convert for numeric use
```

------------------------------------------------------------------------

## 8. Simple Calculator Example (My Practice Code)

``` python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_val = num1 + num2
diff_val = num1 - num2
prod_val = num1 * num2
quot_val = num1 / num2

print("Sum:", sum_val)
print("Difference:", diff_val)
print("Product:", prod_val)
print("Quotient:", quot_val)
```

------------------------------------------------------------------------

These notes help me lock in the fundamentals of Python variables and
data handling.
