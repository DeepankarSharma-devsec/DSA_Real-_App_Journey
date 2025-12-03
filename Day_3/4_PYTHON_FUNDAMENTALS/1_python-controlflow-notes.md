# Personal Notes: Python Control Flow -- Conditional Statements

------------------------------------------------------------------------

## 1. What Control Flow Means (My Understanding)

Control flow decides **which part of my code runs** and **when it
runs**.\
Conditionals (`if`, `elif`, `else`) help my program make decisions.

------------------------------------------------------------------------

## 2. The `if` Statement

Runs a block of code only when the condition is **True**.

``` python
age = 20

if age >= 18:
    print("You are allowed to vote.")
```

------------------------------------------------------------------------

## 3. The `else` Statement

Executes only if the `if` condition is **False**.

``` python
age = 16

if age >= 18:
    print("Eligible for voting.")
else:
    print("You are a minor.")
```

------------------------------------------------------------------------

## 4. The `elif` Statement (Else If)

Used to check **multiple conditions**.

``` python
age = 17

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

------------------------------------------------------------------------

## 5. Nested Conditions

Useful when I need multiple levels of checks.

``` python
number = int(input("Enter number: "))

if number > 0:
    print("Positive")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Zero or Negative")
```

------------------------------------------------------------------------

## 6. Practical Examples

### ✔️ A. Leap Year Checker

``` python
year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
```

------------------------------------------------------------------------

### ✔️ B. Simple Calculator

``` python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")
```

------------------------------------------------------------------------

## 7. Best Practices

-   Indentation is everything in Python.\
-   Always end `if`, `elif`, `else` with a colon (`:`).\
-   Order your conditions logically (most specific first).\
-   Test boundary values (like zero, age limits, etc.).

------------------------------------------------------------------------

These notes keep my understanding of conditional flow crisp before
moving into loops and more complex logic.
