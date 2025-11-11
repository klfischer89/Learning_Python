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

print(names[0]) # access first item -> 'Max'
print(names[-1]) # access last item -> 'Erika'

names.sort() # sort list alphabetically
print(names) # ['Anna', 'Erika', 'Max']
names.reverse() # reverse list
print(names) # ['Max', 'Erika', 'Anna']

print(names[1:3]) # slice list from index 1 to 2 -> ['Erika', 'Anna']
print(names[:2]) # slice list from start to index 1 -> ['Max', 'Erika']
print(names[1:]) # slice list from index 1 to end -> ['Erika', 'Anna']

print(len(names)) # length of list -> 3

print(names.index("Erika")) # find index of 'Erika' -> 1
print(names[1]) # access item at index 1 -> 'Erika'
names.pop(1) # remove item at index 1
print(names) # ['Max', 'Anna']

names.remove("Anna") # remove 'Anna' from list
print(names) # ['Max']

print("Max" in names) # check if 'Max' is in list -> True
print("Susi" in names) # check if 'Susi' is in list -> False

if "Max" in names:
    names.remove("Max") # remove 'Max' if it exists

names.append("Lena") # add 'Lena' to list
print(names) # ['Lena']

l = "Orange, Apfel, Kirsche" # string of fruits
fruit_list = l.split(", ") # split string into list
print(fruit_list) # ['Orange', 'Apfel', 'Kirsche']
print(l) # original string

l = "heute ist ein schöner tag" # string
words = l.split(" ") # split string into list of words
print(words) # ['heute', 'ist', 'ein', 'schöner', 'tag']

l2 = ['Orange', 'Apfel', 'Kirsche'] # list of fruits
joined_string = ", ".join(l2) # join list into string
print(joined_string) # 'Orange, Apfel, Kirsche'

names.clear() # clear all items from list
print(names) # []
