name1 = "Max" # string
name2 = 'Erika' # string

names = ["Max", "Erika", "Susi"] # list of strings
names.append("Moritz") # add string to list
print(names) # ['Max', 'Erika', 'Susi', 'Moritz']

names.insert(1, "Anna") # insert string at index 1
print(names) # ['Max', 'Anna', 'Erika', 'Susi', 'Moritz']
names.remove("Susi") # remove string from list
print(names) # ['Max', 'Anna', 'Erika', 'Moritz']
print(names[2]) # access string at index 2 -> 'Erika'
print(len(names)) # length of list -> 4
for name in names: # iterate over list
    print(name)
# Max
# Anna
# Erika
# Moritz

mixed_list = [1, "Hello", 3.14, True] # list with different data types
print(mixed_list) # [1, 'Hello', 3.14, True]
numbers = list(range(5)) # create list of numbers from 0 to 4
print(numbers) # [0, 1, 2, 3, 4]

print(names.pop()) # remove and return last item -> 'Moritz'
print(names) # ['Max', 'Anna', 'Erika']
