# Personal Notes: Python Lists

------------------------------------------------------------------------

## 1. What Lists Are (My Understanding)

Lists are one of Python's most flexible data structures.

-   **Ordered** → each item has an index\
-   **Mutable** → I can change values anytime\
-   **Heterogeneous** → can store mixed data types

Lists help me store and work with collections of values easily.

------------------------------------------------------------------------

## 2. Creating Lists

### ✔️ Empty List

``` python
my_list = []
```

### ✔️ List of Same-Type Elements

``` python
names = ["Krish", "Jack", "Jacob"]
```

### ✔️ Mixed-Type List

``` python
mixed = [1, "String", 3.14, True]
```

------------------------------------------------------------------------

## 3. Accessing Elements (Indexing & Slicing)

Python uses **0-based indexing**.

### ✔️ Positive Indexing

``` python
fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Guava"]
print(fruits[0])  # Apple
print(fruits[2])  # Cherry
```

### ✔️ Negative Indexing

``` python
print(fruits[-1])  # Guava
```

### ✔️ Slicing Patterns

-   `fruits[1:]` → from index 1 to end\
-   `fruits[1:3]` → index 1 to 2\
-   `fruits[:]` → copy whole list\
-   `fruits[::-1]` → reverse\
-   `numbers[::2]` → skip values

------------------------------------------------------------------------

## 4. Modifying Lists (Because They're Mutable)

``` python
fruits[1] = "Watermelon"
```

------------------------------------------------------------------------

## 5. Common List Methods (Ones I'll Use Most)

  Method         What It Does                           Example
  -------------- -------------------------------------- -----------------------------
  `.append()`    Add at end                             `fruits.append("Orange")`
  `.insert()`    Add at index                           `fruits.insert(1, "Mango")`
  `.remove()`    Remove by value                        `fruits.remove("Banana")`
  `.pop()`       Remove & return last item (or index)   `fruits.pop()`
  `.index()`     Get index of value                     `fruits.index("Cherry")`
  `.count()`     Count occurrences                      `fruits.count("Apple")`
  `.sort()`      Sort ascending                         `fruits.sort()`
  `.reverse()`   Reverse list                           `fruits.reverse()`
  `.clear()`     Empty list                             `fruits.clear()`

------------------------------------------------------------------------

## 6. Looping Through Lists

### ✔️ Simple Loop

``` python
for fruit in fruits:
    print(fruit)
```

### ✔️ Using `enumerate()`

``` python
for index, value in enumerate(fruits):
    print(index, value)
```

------------------------------------------------------------------------

## 7. List Comprehension (My Favorite Shortcut)

### ✔️ Basic Pattern

``` python
new_list = [expression for item in iterable]
```

### Example: Squares

``` python
sq = [x**2 for x in range(10)]
```

### ✔️ With Condition

``` python
even_nums = [num for num in range(10) if num % 2 == 0]
```

### ✔️ Nested Comprehension

``` python
pairs = [[i, j] for i in [1, 2] for j in ['a', 'b']]
```

### ✔️ Using Built-in Functions

``` python
words = ["Hello", "World", "Python"]
lengths = [len(word) for word in words]  # [5, 5, 6]
```

------------------------------------------------------------------------

## Conclusion

Lists are powerful because they're:

-   Flexible\
-   Mutable\
-   Great for iteration\
-   Even better with comprehension

Mastering slicing + comprehension = writing clean, Pythonic code.
