# OOP in Python — Abstraction (My Notes)

## 1. What Abstraction Really Means (How I Think About It)

Abstraction is all about **hiding complexity** and showing only what’s essential.  
I interact with a simple interface, while the messy internal logic stays hidden.

Examples that make it easy to understand:
- **Washing machine:** I press “Start,” but I don’t need to know how the motor spins.
- **Car:** I use the accelerator and brakes without understanding engine mechanics.

OOP abstraction works exactly like this.

---

## 2. How Python Implements Abstraction

Python uses **Abstract Base Classes (ABCs)** to enforce abstraction.

Key components I need to remember:
- `ABC` → Marks a class as abstract.
- `@abstractmethod` → Forces subclasses to implement certain methods.
- Abstract classes **cannot be instantiated**.

---

## 3. Vehicle Example (My Preferred Breakdown)

### Step 1: Create an Abstract Base Class

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    # A normal (concrete) method
    def drive(self):
        print("The vehicle is used for driving")

    # An abstract method that MUST be implemented by subclasses
    @abstractmethod
    def start_engine(self):
        pass
```

The abstract class defines:
- **What** every vehicle should be able to do.
- Not **how** each vehicle does it.

---

### Step 2: Concrete Class Implements Hidden Logic

```python
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
```

If I forget to implement `start_engine`, Python won't let me create a `Car` object.  
This enforces consistency.

---

### Step 3: Using the Abstraction

```python
def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car1 = Car()
operate_vehicle(car1)
```

**Output:**
```
Car engine started
The vehicle is used for driving
```

The function doesn’t care *which* vehicle it receives.  
It only cares that the object follows the `Vehicle` interface — this is the power of abstraction.

---

## 4. Why This Matters (My Takeaways)

- Abstraction hides unnecessary details and exposes only what’s required.
- It gives me a clean interface and forces structure through abstract methods.
- Helps in large systems where different subclasses share the same required behaviors.
- The parent defines the **contract**, the child supplies the **implementation**.

---

## Summary Table

| Concept | Meaning | Python Feature |
|--------|---------|----------------|
| Abstract Class | Blueprint that cannot be instantiated | `class Vehicle(ABC)` |
| Abstract Method | A required method with no implementation | `@abstractmethod` |
| Concrete Class | Implements all abstract methods | `class Car(Vehicle)` |
| Interface Guarantee | Every subclass follows same structure | Enforced by ABC |

This completes my notes on abstraction — the final OOP pillar that ties everything cleanly together.
