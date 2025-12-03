# Personal Notes: Python Loops -- Iteration & Control Flow

------------------------------------------------------------------------

## 1. What Loops Mean (My Understanding)

Loops help me repeat actions without writing the same code again and
again.\
Python mainly uses:

-   **for loops** → for sequences\
-   **while loops** → for conditions

------------------------------------------------------------------------

## 2. For Loop

The `for` loop lets me iterate over sequences like lists, strings, or
numbers using `range()`.

### ✔️ Understanding `range(start, stop, step)`

-   **start** → beginning (default 0)\
-   **stop** → end (exclusive)\
-   **step** → increment (default 1)

### Examples

#### Basic Loop

``` python
for i in range(5):
    print(i)   # 0 to 4
```

#### Custom Start/Stop

``` python
for i in range(1, 6):
    print(i)   # 1 to 5
```

#### Using Step

``` python
for i in range(1, 10, 2):
    print(i)   # 1, 3, 5, 7, 9
```

#### Reverse Loop

``` python
for i in range(10, 1, -1):
    print(i)   # 10 down to 2
```

### ✔️ Iterating Through Strings

``` python
name = "Krish"
for c in name:
    print(c)
```

------------------------------------------------------------------------

## 3. While Loop

Runs as long as the condition is **True**.\
I must update the loop variable manually, or I'll create an infinite
loop.

``` python
count = 0
while count < 5:
    print(count)
    count += 1
```

------------------------------------------------------------------------

## 4. Loop Control Statements

### ✔️ A. `break`

Stops the loop immediately.

``` python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### ✔️ B. `continue`

Skips the current iteration and moves to the next.

``` python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # Prints odd numbers
```

### ✔️ C. `pass`

Placeholder --- does nothing.

``` python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

------------------------------------------------------------------------

## 5. Nested Loops

A loop inside another loop.

``` python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

------------------------------------------------------------------------

## 6. Practical Examples

### ✔️ Example 1: Sum of First N Natural Numbers

``` python
n = 10
sum_val = 0
count = 1

while count <= n:
    sum_val += count
    count += 1

print(sum_val)  # 55
```

------------------------------------------------------------------------

### ✔️ Example 2: Prime Numbers (For--Else Concept)

The `else` block runs only if the loop **did not break**.

``` python
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
```

------------------------------------------------------------------------

These notes help me keep the logic of loops crystal clear, especially
`break`, `continue`, and the powerful `for–else` combination.
