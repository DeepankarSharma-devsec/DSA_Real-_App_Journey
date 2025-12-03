# Personal Notes: Python Operators

------------------------------------------------------------------------

## 1. Introduction

Operators are the core building blocks of logic and calculations in
Python.\
They help me perform math, compare values, and build complex conditions.

------------------------------------------------------------------------

## 2. Arithmetic Operators (The Basics I Always Use)

These work with numeric values.

``` python
a = 10
b = 5
c = 21
```

### ✔️ Common Arithmetic Operators

-   `+` → Addition\
-   `-` → Subtraction\
-   `*` → Multiplication\
-   `/` → Division (always returns **float**)\
-   `//` → Floor division (drops decimal)\
-   `%` → Modulus (remainder)\
-   `**` → Exponent (power)

### ✔️ Example Outputs

``` python
print(a + b)   # 15
print(c / b)   # 4.2
print(c // b)  # 4
print(a % b)   # 0
print(a ** 2)  # 100
```

------------------------------------------------------------------------

## 3. Comparison Operators (Return True/False)

These compare two values and always return a boolean.

-   `==` → Equal to\
-   `!=` → Not equal to\
-   `>` → Greater than\
-   `<` → Less than\
-   `>=` → Greater than or equal to\
-   `<=` → Less than or equal to

Case sensitivity matters when comparing strings.

``` python
a = 10
b = 10
str1 = "Chris"
str2 = "chris"

print(a == b)       # True
print(str1 == str2) # False
print(a != 15)      # True
print(a >= 10)      # True
```

------------------------------------------------------------------------

## 4. Logical Operators (Used for Conditions)

I use these to combine multiple comparisons.

### ✔️ AND (`and`)

True only if **both** conditions are true.

### ✔️ OR (`or`)

True if **at least one** condition is true.

### ✔️ NOT (`not`)

Reverses the boolean value.

``` python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

------------------------------------------------------------------------

## 5. Practical Example: Mini Calculator

A simple project using arithmetic operators and typecasting.

``` python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Diff:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Remainder:", num1 % num2)
print("Power:", num1 ** num2)
```

------------------------------------------------------------------------

These notes help me keep operator behavior fresh, especially before
jumping into conditionals and loops.
