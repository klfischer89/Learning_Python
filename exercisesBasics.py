w = 3   # Integer
# Check if w is even or odd
if w % 2 == 0:
    print(w, "w is even")
else:
    print(w, "w is odd")

zws = 47.6 # Float

if zws < 50:
    zws_missing = round(50 - zws, 2) # Calculate missing amount to reach 50
    print("You need", zws_missing, "more to reach 50") # Output the missing amount

    zws = zws + 7.95 # Update zws by adding 7.95
    print("New zws value:", round(zws)) # Output the new zws value
else:
    print("zws is already 50 or more", round(zws)) # Output the current zws value

print("Hallo {:2.f}!".format(zws)) # Formatted output of zws