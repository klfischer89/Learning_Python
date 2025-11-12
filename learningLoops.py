for i in range(1,11): # prints numbers from 1 to 100
    print(i)

print(list(range(1,11))) # prints a list of numbers from 1 to 100

for i in [1, 13, 42, 55]: # prints each number in the list
    print(i)
    print("Hallo Welt:", i) # prints "Hallo Welt:" followed by each number in the list
    print("Hallo Welt:" + str(i)) # prints "Hallo Welt:" followed by each number in the list, converting number to string

numbers = [3, 5, 7, 9, 11] # defines a list of numbers
for number in numbers: # iterates through each number in the list
    print(number) # prints each number

s = 0 # initializes sum variable
for i in range(1,101): # adding numbers from 1 to 100
    s += i
print(s) # prints the sum of numbers from 1 to 100

print(sum(range(1,101))) # prints the sum of numbers from 1 to 100 using built-in sum function

text = "Hallo Welt" # defines a string
for char in text: # iterates through each character in the string
    print(char) # prints each character

for char in text.lower(): # iterates through each character in the lowercase version of the string
    print(char) # prints each character

final = "" # initializes an empty string
for char in text: # iterates through each character in the string
    print(char + ".") # prints each character followed by a period
    final = final + char + "." # appends each character followed by a period to the final string
print(final) # prints the final string with periods after each character

names = ["Alice", "Bob", "Charlie"] # defines a list of names
for name in names: # iterates through each name in the list
    print(name) # prints each name
    print("Hallo " + name + "!") # prints a greeting for each name

greetings = [] # initializes an empty list for greetings
for name in names: # iterates through each name in the list
    greetings.append("Hallo " + name + "!") # appends a greeting for each name to the greetings list
print(greetings) # prints the list of greetings

lengths = [] # initializes an empty list for name lengths
for name in names: # iterates through each name in the list
    lengths.append(len(name)) # appends the length of each name to the lengths list
print(lengths) # prints the list of name lengths

greetings = [ "Hallo " + name + "!" for name in names ] # list comprehension for greetings
print(greetings) # prints the list of greetings

lengths = [ len(name) for name in names ] # list comprehension for name lengths
print(lengths) # prints the list of name lengths
squares = [ i**2 for i in range(1,11) ] # list comprehension for squares of numbers from 1 to 10
print(squares) # prints the list of squares
evens = [ i for i in range(1,21) if i % 2 == 0 ] # list comprehension for even numbers from 1 to 20
print(evens) # prints the list of even numbers
cubes = [ i**3 for i in range(1,11) if i % 2 != 0 ] # list comprehension for cubes of odd numbers from 1 to 10
print(cubes) # prints the list of cubes of odd numbers
filtered_names = [ name for name in names if len(name) > 3 ] # list comprehension for names longer than 3 characters
print(filtered_names) # prints the list of filtered names

numbers3 = [number for number in range(1,101) if number % 3 == 0 ] # list comprehension for numbers from 1 to 100 that are multiples of 3
print(numbers3) # prints the list of numbers that are multiples of 3

a = 23 # defines variable a
while a >= 0: # continues while a is non-negative
    print(a) # prints the value of a
    a -= 1 # decrements a by 1

for i in range(1, 11): # prints numbers from 1 to 10
    if i != 5 and i != 8: # skips numbers 5 and 8
        print(i) # prints the value of i

for i in range(1, 11): # prints numbers from 1 to 10
    if i == 5:
        continue # skips the rest of the loop when i is 5
    if i == 8:
        break # exits the loop when i is 8
    print(i) # prints the value of i