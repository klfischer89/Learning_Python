# learningStrings.py
print("Hallo Welt")
print("Hallo" + " " + "Welt")
print("Hallo" * 3)

print("Hallo" + " Welt!" + str(3)) # Concatenation with a number converted to string
print(len("Hallo Welt!")) # Length of the string
print("Welt" in "Hallo Welt!") # Check substring presence

what = "     banana    " # String with leading and trailing spaces
what = what.strip() # Remove leading and trailing spaces
print(what.strip()) # Print the stripped string
print(what.upper()) # Convert to uppercase
print(what.lower()) # Convert to lowercase
print(what.replace("banana", "apple")) # Replace substring
print(what.split("a")) # Split string by 'a'

print("This is a string with\nmultiple lines.") # Newline character
print("This is a string with\ttabs.") # Tab character
print("C:\\Users\\Name") # Escape backslash
print(r"C:\Users\Name") # Raw string to ignore escape sequences

print("Hallo Welt".replace("Welt", "Universe")) # Replace 'Welt' with 'Universe'
print("Hallo Welt".find("Welt")) # Find the index of substring 'Welt'
print("Hallo Welt".find("Universe")) # Find substring that doesn't exist

s = "Hallo Welt"
print(s.index("Welt")) # Find the index of substring 'Welt'
print(s.count("l")) # Count occurrences of 'l'
print(s.startswith("Hallo")) # Check if string starts with 'Hallo'