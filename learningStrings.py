# learningStrings.py

print("Hallo Welt") # Simple string output
print("Hallo" + " " + "Welt") # String concatenation
print("Hallo" * 3) # String repetition

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

txt = "Hallo Welt!"
print(txt[0])    # First character
print(txt[2:5])  # Characters from index 2 to 4
print(txt[:5])   # Characters from start to index 4
print(txt[6:])   # Characters from index 6 to end
print(txt[-1])   # Last character
print(txt[-5:-2]) # Characters from index -5 to -3
print(txt.format("Python")) # Using format method

s = "Das Beste kommt zum Schluss. Dann ist wirklich Schluss." # Original string
r = s.replace("Schluss", "Ende", 1) # Replace only the first occurrence of 'Schluss' with 'Ende'
print(r) # Print the modified string

r = "close_file = Schließe die Datei" # String with special character
r = r[r.find("=") + 1:-1].strip() # Extract substring after '=' and strip spaces
print(r) # Print the extracted substring

s = "Fischers Fritz fischt frische Fische" # Original string
s = s[:17] + "..." # Truncate string and add ellipsis
print(s) # Print the truncated string with ellipsis

s_teaser = s[:17] # Create teaser substring
s_teaser_pos = s_teaser.rfind(" ") # Find last space in teaser
s_teaser = s_teaser[:s_teaser_pos] + "..." # Truncate at last space and add ellipsis
print(s_teaser) # Print the final teaser string