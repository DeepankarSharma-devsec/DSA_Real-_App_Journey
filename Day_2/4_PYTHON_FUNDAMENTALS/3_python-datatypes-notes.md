# Personal Notes: Python Data Types

------------------------------------------------------------------------

## 1. What Data Types Mean (My Understanding)

Data types define **what kind of data** I'm working with and **how
Python interprets it**.

They determine: - Which operations are allowed\
- How much memory is used\
- What kind of errors might occur

Understanding data types early makes code more reliable and predictable.

------------------------------------------------------------------------

## 2. Basic Python Data Types

### ✔️ A. Integers (`int`)

Whole numbers.

``` python
age = 35
print(type(age))  # <class 'int'>
```

------------------------------------------------------------------------

### ✔️ B. Floating Point Numbers (`float`)

Numbers with decimals.

``` python
height = 5.11
print(type(height))  # <class 'float'>
```

------------------------------------------------------------------------

### ✔️ C. Strings (`str`)

Any text wrapped in quotes.

``` python
name = "Chris"
print(type(name))  # <class 'str'>
```

------------------------------------------------------------------------

### ✔️ D. Booleans (`bool`)

Represents truth values.

``` python
is_true = True
print(type(is_true))

a = 10
b = 10
print(a == b)  # True
```

------------------------------------------------------------------------

## 3. Type Conversion & Common Mistakes

### ❌ Example of a Type Error

Trying to combine a string with a number:

``` python
result = "Hello" + 5
```

Error:

    TypeError: can only concatenate str (not "int") to str

### ✔️ Correct Way: Convert Number to String

``` python
result = "Hello" + str(5)
print(result)  # Hello5
```

------------------------------------------------------------------------

## 4. What's Coming Next

These are the core basics before diving deeper into: - Lists - Tuples -
Sets - Dictionaries - Operators - String methods

These topics all build on today's foundation.

------------------------------------------------------------------------

These notes help me stay clear on how Python handles data before moving
to complex structures.
