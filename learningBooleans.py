b = True # Assigning a boolean value
print(b) # Simple boolean output
print(not b) # Negation of boolean

b2 = False # Another boolean value
print(b2) # Output the second boolean

a = 42  # Assigning an integer value
print(a == 42) # Check equality
print(a != 42) # Check inequality

print(a < 50)  # Less than
print(a <= 42) # Less than or equal to
print(a > 10)  # Greater than
print(a >= 42) # Greater than or equal to

c = "Hallo" # Assigning a string value
print(c == "Hallo") # Check string equality
print(c != "Welt")  # Check string inequality

print(True and False) # Logical AND
print(True or False)  # Logical OR
print((a == 42) and (c == "Hallo")) # Combined logical operations
print((a != 42) or (c == "Welt"))   # Combined logical operations

# Additional boolean operations
print(b and b2) # AND operation between two booleans
print(b or b2)  # OR operation between two booleans
print(b ^ b2)   # XOR operation between two booleans
print(bool(0))  # Convert integer 0 to boolean
print(bool(1))  # Convert integer 1 to boolean

print(not True)  # Negation of True
print(not False) # Negation of False

zahl = 42
print(zahl >= 40 and zahl <= 50) # Check if zahl is between 40 and 50
print(40 <= zahl <= 50)          # Alternative way to check if zahl is between 40 and 50