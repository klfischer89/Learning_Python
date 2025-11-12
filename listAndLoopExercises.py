imperial = [24.3, 25.2, 17.8, 15.4, 21.2, 22.5, 19.7, 18.9] # inches
metric = [] # cm
for i in imperial: # inches to cm
    cm = i * 2.54
    metric.append(cm)
print(metric) # [61.722, 64.008, 45.212, 39.116, 53.848, 57.15, 50.038, 48.006]

metric1 = [i * 2.54 for i in imperial] # list comprehension
print(metric1) # [61.722, 64.008, 45.212, 39.116, 53.848, 57.15, 50.038, 48.006]

itmes = ["book", "laptop", "mouse", "keyboard"]
print(itmes) # ['book', 'laptop', 'mouse', 'keyboard']
ritmes = [item for item in reversed(itmes)] # reverse using list comprehension
print(ritmes) # ['keyboard', 'mouse', 'laptop', 'book']
