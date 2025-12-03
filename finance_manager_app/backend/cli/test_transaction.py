from cli.transaction import Transaction

# Create a few sample transactions
t1 = Transaction(500, "Food", note="Lunch with friend")
t2 = Transaction(1500, "Shopping", "2025-01-01", "New Year purchase")
t3 = Transaction(99.99, "Snacks")

# Print representations
print("REPR OUTPUT:")
print(t1)
print(t2)
print(t3)
print()

print("DICT OUTPUT:")
print(t1.to_dict())
print(t2.to_dict())
print(t3.to_dict())
