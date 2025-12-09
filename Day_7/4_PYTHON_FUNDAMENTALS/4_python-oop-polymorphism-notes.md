# OOP in Python — Polymorphism (My Notes)

## 1. What Polymorphism Really Means (How I Understand It)

Polymorphism lets me write code where **one function can work with many different object types**.  
The objects differ internally, but they expose the *same* method name.

Examples I like:
- `Dog.speak()` and `Cat.speak()` behave differently even though the method name is the same.
- A `print_area()` function works for both `Rectangle` and `Circle`.

This keeps code flexible and clean.

---

## 2. Method Overriding (Core of Polymorphism)

### Base → Derived pattern

```python
class Animal:
    def speak(self):
        return "Sound of the animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
```

### Generic function working with all Animals

```python
def animal_speak(animal):
    print(animal.speak())
```

The power is: **the function doesn’t care which animal it receives**.

---

## 3. Polymorphism in Action — Shape Example

### Base Class

```python
import math

class Shape:
    def area(self):
        return "Generic area"
```

### Children Override the Same Method

```python
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r
```

### Single function handles both

```python
def print_area(shape):
    print("Area:", shape.area())
```

---

## 4. Abstract Base Classes (Enforced Polymorphism)

Sometimes I want to force every subclass to implement a method.  
That is where **ABC + @abstractmethod** is useful.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
```

### Children *must* implement `start_engine`

```python
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
```

### Polymorphic behavior

```python
def start_vehicle(v):
    print(v.start_engine())
```

---

## 5. My Takeaways

- Same interface, different behavior = **Polymorphism**.
- Method overriding is the simplest and most common form.
- ABCs help enforce consistent method definitions across subclasses.
- Keeps functions *generic*, which massively improves code reusability.

This wraps up polymorphism — next step is to build larger systems that rely on these patterns.
