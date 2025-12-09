# OOP in Python — Encapsulation (My Notes)

## 1. What Encapsulation Really Means (My Understanding)

Encapsulation is about **protecting data** inside a class and exposing only what should be publicly accessible.  
It groups:
- **Data (attributes)**
- **Behavior (methods)**  
into one controlled unit.

Why I like this idea:
- Prevents accidental modification.
- Gives a clean interface (like buttons on a washing machine, while internals are hidden).
- Lets me enforce validation using setters.

---

## 2. Python’s Access Levels (By Convention)

Unlike Java/C++, Python doesn’t strictly enforce access control.  
Instead, it uses naming conventions:

### ✔ Public  
`self.name`  
Can be accessed from anywhere.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

### ✔ Protected  
`self._name`  
Meant for internal use or subclasses.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
```

---

### ✔ Private  
`self.__name`  
Triggers **name mangling** → becomes `_Person__name`.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
```

Trying to access `obj.__name` will fail.

---

## 3. Encapsulation via Getters and Setters

Private data should be accessed and modified through controlled methods.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter with validation
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")
```

### Usage

```python
p = Person("Krish", 34)

print(p.get_name())
print(p.get_age())

p.set_age(35)
p.set_age(-5)  # Invalid
```

---

## 4. Summary Table

| Modifier | Syntax | Visibility | Real Use |
|---------|--------|------------|----------|
| Public | `self.name` | Everywhere | Normal attributes |
| Protected | `self._name` | Class + subclasses | Internal use |
| Private | `self.__name` | Only inside class | Sensitive data |

Name mangling does this automatically:
```
__name → _Person__name
```

(Not meant to be used directly, but technically possible.)

---

## My Takeaways

- Encapsulation = controlled access + data protection.
- Private variables keep objects safe from accidental misuse.
- Setters give me a place to add validation logic.
- Clean code becomes easier when internal details are hidden.

Next step: Combine encapsulation with inheritance & polymorphism to build truly modular systems.
