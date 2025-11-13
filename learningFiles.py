f = open("files/faust.txt", "r", encoding="utf-8") # 
# Open the file in read mode with UTF-8 encoding

for l in f: # Iterate through each line in the file
    print(l.strip()) # Print the line without leading/trailing whitespace
    break # Exit the loop after the first line

f.close() # Close the file after reading