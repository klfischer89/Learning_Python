# learningFunctions.py

def f(): # This function prints Hello, World!
    print("Hello, World!")
f() # Call the function to execute it

def g(n): # This function prints numbers from 0 to n-1
    for i in range(n):
        print(i)    
g(5) # Call the function with argument 5

def h(n): # This function returns the square of n
    return n * n
result = h(4) # Call the function with argument 4
print(result) # Print the result

def add(x, y): # This function returns the sum of x and y
    return x + y
sum_result = add(3, 7) # Call the function with arguments 3 and 7
print(sum_result) # Print the sum result

def b(n = 10): # This function prints numbers from 0 to n-1 with a default value of 10
    for i in range(n):
        print(i)
b() # Call the function without argument, uses default value
b(3) # Call the function with argument 3

def z (a, b): # This function returns both a and b
    print("a =", str(a))
    print("b =", str(b))
z(b=5, a=10) # Call the function with named arguments

import math # Import the math module

print(math.sqrt(16)) # Use the sqrt function from the math module to print the square root of 16

def add1(x, y): # This function returns the sum of x and y
    return x + y
print(add1(2, 3)) # Call the function with arguments 2 and 3 and print the result
print(add1(y=7, x=4)) # Call the function with named arguments and print the result
print(add1(1,1) + 2) # Call the function and add 2 to the result, then print it

def max2(a, b): # This function returns the maximum of a and b
    if a > b:
        return a
    else:
        return b
print(max2(10, 20)) # Call the function with arguments 10 and 20 and print the result

