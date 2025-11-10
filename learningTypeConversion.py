z = str(52)  # Converting integer to string
print(z + "!")  # Concatenating string with "!"

z1 = "42" # String representing a number
z2 = "13" # Another string representing a number
print(z1 + z2)  # Concatenating two strings
print(int(z1) + int(z2))  # Converting strings to integers and adding
print(float(z1) + float(z2))  # Converting strings to floats and adding
z3 = 3.14159 # A float number
print(str(z3) + " is Pi")  # Converting float to string and concatenating
print(int(z3))  # Converting float to integer (truncation)
print(float(int(z3)))  # Converting float to integer and back to float

print(abs(-42))  # Absolute value
print(complex(3, 4))  # Creating a complex number

b = 0 # Integer zero
print(bool(b))  # Converting integer 0 to boolean
b2 = 42 # Non-zero integer
print(bool(b2))  # Converting non-zero integer to boolean
s = "" # Empty string
print(bool(s))  # Converting empty string to boolean
s2 = "Hallo" # Non-empty string
print(bool(s2))  # Converting non-empty string to boolean

# Demonstrating type conversion in expressions
a = "The answer is " + str(42)  # Concatenating string with converted integer
print(a)  # Output the result
b = 3.14 * int("10")  # Multiplying float with converted integer
print(b)  # Output the result
c = float("2.5") + 4.5  # Adding converted float to another float
print(c)  # Output the result
d = complex(1, 2) + complex(int("3"), int("4"))  # Adding complex numbers with converted integers
print(d)  # Output the result
# Converting boolean to integer and float
bool_val = True
print(int(bool_val))  # Convert boolean True to integer
print(float(bool_val))  # Convert boolean True to float
bool_val2 = False
print(int(bool_val2))  # Convert boolean False to integer
print(float(bool_val2))  # Convert boolean False to float
# Converting between different numeric types
int_num = 7 # An integer number
float_num = float(int_num)  # Convert integer to float
print(float_num)  # Output the float number
float_num2 = 3.99 # A float number
int_num2 = int(float_num2)  # Convert float to integer (truncation
print(int_num2)  # Output the integer number