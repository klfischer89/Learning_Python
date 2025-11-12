words = {"river" : "Fluss",
          "city" : "Stadt"} # dictionary with key and value
print(words["river"]) # access value by key

words["mountain"] = "Berg" # add new key-value pair
print(words) # print entire dictionary

print(len(words)) # number of key-value pairs

w = "city" # variable holding key
print(words[w]) # access value using variable as key

for key, value in words.items(): # iterate through key-value pairs
    print(f"{key} means {value} in German.") # formatted output

for x in words.items(): # iterate through items
    print(x) # print each item (tuple)

print(list(words.items())) # convert items to list of tuples

words_list = list(words.items()) # store items as list of tuples
print(words_list[0]) # access first tuple
key, value = words_list[0] # unpack first tuple
print(f"Key: {key}, Value: {value}") # print unpacked values

print(words.keys()) # print all keys
print(words.values()) # print all values

print("river" in words) # check if key exists
print("ocean" in words) # check for non-existing key

if "ocean" not in words: # conditional check
    words["ocean"] = "Ozean" # add new key-value pair

if not "mountain" in words: # another conditional check
    words["mountain"] = "Berg" # add new key-value pair

del words["city"] # delete key-value pair
print(words) # print updated dictionary

if "city" in words: # check before deletion
    del words["city"] # delete if exists