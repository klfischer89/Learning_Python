elements = [3, 9, 16, 25, 36, 49,81] # list of integers
print(elements) # [3, 9, 16, 25, 36, 49, 81]

elements.append(100) # add 100 to the end of the list
print(elements) # [3, 9, 16, 25, 36, 49, 81, 100]

elements.insert(0, 1) # insert 1 at index 0
print(elements) # [1, 3, 9, 16, 25, 36, 49, 81, 100]

pos = elements.index(49) # find index of 49
elements.insert(pos + 1, 64) # insert 64 after 49
print(elements) # [1, 3, 9, 16, 25, 36, 49, 64, 81, 100]

print(len(elements)) # length of list -> 10
l = int(len(elements) / 2) # calculate half length
print(l) # 5
elements1 = elements[:l] # slice first half
elements2 = elements[l:] # slice second half
print(elements1) # [1, 3, 9, 16, 25]
print(elements2) # [36, 49, 64, 81, 100]
