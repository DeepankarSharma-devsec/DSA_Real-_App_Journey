# OOP in Python — Inheritance (My Notes)

## 1. What Inheritance Means (My Understanding)

Inheritance lets one class **reuse** and **extend** another class’s attributes and behaviors.  
I like the real-life analogy: a child inheriting property from parents — the flow is always **Parent → Child**.

Why I find inheritance useful:
- Avoids rewriting the same code
- Keeps relationships between classes clean
- Models real-world hierarchies (Car → Tesla, Animal → Dog, etc.)

---

## 2. Single Inheritance

One parent, one child.

### Parent Class

```python
class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):
        print(f"The person will drive the {self.engine_type} car")
```

### Child Class (using `super()`)

```python
class Tesla(Car):
    def __init__(self, windows, doors, engine_type, is_self_driving):
        super().__init__(windows, doors, engine_type)
        self.is_self_driving = is_self_driving

    def self_driving(self):
        print(f"Tesla supports self-driving: {self.is_self_driving}")
```

### Usage

```python
tesla1 = Tesla(4, 5, "electric", True)
tesla1.self_driving()
tesla1.drive()  # inherited
```

---

## 3. Multiple Inheritance

One child inherits from **two parents**.

### Parent Classes

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclasses must implement this method")

class Pet:
    def __init__(self, owner):
        self.owner = owner
```

### Child Class (inherits from both)

```python
class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says Woof"
```

### Usage

```python
dog = Dog("Buddy", "Krish")
print(dog.speak())
print(dog.owner)
```

---

## 4. Notes I Keep in Mind

- `super()` is great for single inheritance; multiple inheritance needs explicit parent calls.
- If a child class defines a method with the same name as its parent, it **overrides** the parent’s method.
- Always structure inheritance when it reflects a real **“is-a”** relationship:
  - Tesla *is a* Car
  - Dog *is an* Animal

---

## 5. Quick Reference Table

| Concept | Meaning |
|--------|---------|
| `class Child(Parent)` | Defines inheritance |
| `super().__init__()` | Calls parent constructor |
| `Parent.__init__(self)` | Explicit constructor call (multiple inheritance) |
| Overriding | Child method replaces parent method |

---

Next steps: model a full Library Management System using inheritance patterns — will be great for practicing real-world OOP.
