# Object-Oriented Programming (OOP) in Python — My Notes

### 1. Introduction

OOP lets me structure programs around **real-world entities**.  
Instead of writing scattered functions and variables, I build **classes** (blueprints) and then create **objects** (instances).  
It keeps code clean, reusable, and easier to scale.

---

### 2. Class vs Object (My Mental Model)

- **Class:** A blueprint. Defines attributes + behaviors.
- **Object:** A real usable thing created from the class.

I always remember the car analogy:
- *Class = car blueprint*
- *Object = actual Audi, BMW, etc.*

---

### 3. Creating Classes and Objects

```python
class Car:
    pass

audi = Car()
bmw = Car()

print(type(audi))
```

At this point, the class has no attributes or behaviors.

---

### 4. Attributes + The Constructor (`__init__`)

Best practice: define attributes **in the constructor** instead of randomly attaching them.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

`self` always refers to the current object.

Usage:

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 4)

print(dog1.name)
print(dog2.name)
```

---

### 5. Instance Methods (Object Behaviors)

Methods are functions *inside* a class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")
```

Calling a method:

```python
dog1 = Dog("Buddy", 3)
dog1.bark()
```

---

### 6. Real Example I Like: Bank Account Model

Great way to understand state, behavior, and object interaction.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def get_balance(self):
        return self.balance
```

Usage:

```python
account = BankAccount("Krish", 5000)
account.deposit(100)
account.withdraw(300)
account.withdraw(6000)
print(account.get_balance())
```

---

### 7. Best Practices I Keep in Mind

- Class names use **PascalCase** (e.g., `BankAccount`).
- Always define instance variables in the constructor.
- Use `self` to refer to attributes and methods of the current object.
- Use OOP when modeling real-world things or when code gets complex.
- Keep methods focused: each method should do *one* logical operation.

---

OOP becomes powerful once I start thinking in terms of *entities* and *behaviors*. These fundamentals set the stage for inheritance, polymorphism, abstraction, and encapsulation later on.
