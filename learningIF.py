z = 42  # Assigning an integer value
# Simple if statement to check the value of z
if z < 50 and z > 10:  
    print("z is less than 50") 

txt = "Hallo Welt" # Assigning a string value
if txt:  # Check if the string is non-empty
    print("The string is not empty")

p = 42 # Assigning another integer value
if p:  # Check if p is non-zero
    print("p is non-zero")  

if z > 10:  # Check if z is greater than 10
    print("z is greater than 10")
else :  # If z is not greater than 10
    print("z is not greater than 10")

# Nested if-else statements
if z > 10:  # Check if z is greater than 10
    print("z is greater than 10")
else :  # If z is not greater than 10
    if z < 5:  # Check if z is less than 5
        print("z is less than 5")
    else :  # If z is neither greater than 10 nor less than 5
        print("z is not greater than 10")

# Using elif for multiple conditions
if z > 50:  # Check if z is greater than 50
    print("z is greater than 50")
elif z > 10:  # Check if z is greater than 10
    print("z is greater than 10 but not greater than 50")
else :  # If z is neither greater than 50 nor greater than 10
    print("z is 10 or less")

# More complex conditions with elif
if z > 100:  # Check if z is greater than 100
    print("z is greater than 100")
elif z > 50:  # Check if z is greater than 50
    print("z is greater than 50 but not greater than 100")
elif z > 10:  # Check if z is greater than 10
    print("z is greater than 10 but not greater than 50")
else :  # If z is 10 or less
    print("z is 10 or less")