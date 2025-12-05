# Personal Notes: Python Tuples

------------------------------------------------------------------------

## 1. What Tuples Are (My Understanding)

Tuples behave a lot like lists, **but they cannot be changed**.\
That immutability is their superpower --- especially when I want data to
stay fixed.

-   **Ordered** (indexed)
-   **Immutable** (no modifications)
-   **Can store mixed data types**

------------------------------------------------------------------------

## 2. Creating Tuples

### ✔️ Empty Tuple

``` python
my_tuple = ()
my_tuple = tuple()
```

### ✔️ Homogeneous

``` python
numbers = (1, 2, 3, 4, 5, 6)
```

### ✔️ Mixed Types

``` python
mixed = (1, "Hello", 3.14, True)
```

### ✔️ Convert List ↔ Tuple

``` python
lst = [1, 2, 3]
tup = tuple(lst)
lst_back = list(tup)
```

------------------------------------------------------------------------

## 3. Accessing Elements

### ✔️ Indexing

``` python
print(numbers[0])
print(numbers[-1])
```

### ✔️ Slicing

``` python
print(numbers[0:4])
print(numbers[::-1])
```

------------------------------------------------------------------------

## 4. Tuple Operations

### ✔️ Concatenation

``` python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
```

### ✔️ Repetition

``` python
repeated = t1 * 3
```

------------------------------------------------------------------------

## 5. Immutability (The Key Feature)

Trying to modify a tuple raises an error:

``` python
my_tuple = (1, 2, 3)
my_tuple[1] = "Krish"   # Error
```

### ✔️ Workaround

Convert → Modify → Convert back:

``` python
lst = list(my_tuple)
lst[1] = "Krish"
my_tuple = tuple(lst)
```

------------------------------------------------------------------------

## 6. Tuple Methods

Fewer methods because tuples are immutable.

### ✔️ `.count()`

``` python
t = (1, 2, 3, 1, 1)
t.count(1)   # 3
```

### ✔️ `.index()`

``` python
t.index(2)   # 1
```

------------------------------------------------------------------------

## 7. Packing & Unpacking

### ✔️ Packing

``` python
packed = 1, "Hello", 3.14
```

### ✔️ Unpacking

``` python
a, b, c = packed
```

### ✔️ Unpacking with `*`

``` python
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
```

-   `middle` becomes a **list** of all the in-between values.

------------------------------------------------------------------------

## 8. Nested Tuples

Tuples can hold other tuples.

``` python
nested = ((1, 2, 3), ("a", "b", "c"), (True, False))
```

### ✔️ Accessing Inside

``` python
nested[0]        # (1,2,3)
nested[1][2]     # 'c'
```

### ✔️ Iterating

``` python
for sub in nested:
    for item in sub:
        print(item, end=" ")
    print()
```

------------------------------------------------------------------------

## Why Tuples Matter

-   They're faster than lists\
-   They ensure data safety (immutability)\
-   They can be used as dictionary keys (lists cannot)\
-   Great for fixed data like coordinates, config values, etc.

------------------------------------------------------------------------

These notes strengthened my understanding of when to choose tuples over
lists --- mainly when I need reliability and speed.
