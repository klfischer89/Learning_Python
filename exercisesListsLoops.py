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

new_cases = [40,42,46,42,40,38,36,30,32,34,36,35,34,33,32,16,23,16,23,24,25,16,4,5,6,3,2,2] # daily new cases
rValues = [] # R values

for value in range(1, len(new_cases)): # loop through new cases list
    rValues.append(round(new_cases[value] / new_cases[value - 1], 2)) # calculate R values

print(rValues) # [1.05, 1.09, 0.91, 0.95, 0.9, 0.84, 0.83, 1.07, 1.06, 1.06, 0.97, 0.97, 0.97, 0.94, 0.5, 1.44, 0.7, 1.44, 1.04, 1.04, 0.64, 0.25, 1.25, 1.2, 0.5, 0.67, 1.0]

temperatures = [20.4, 21.2, 21.4, 23.7, 18.9, 15.4, 15.0, 28.8, 29.6, 29.8, 33.4, 33.8, 32.9, 29.0, 22.2 ] # daily temperatures in Celsius
fahrenheit = [] # temperatures in Fahrenheit
for temp in temperatures: # loop through temperatures list
    f = (temp * 9/5) + 32 # convert to Fahrenheit
    fahrenheit.append(round(f, 1)) # append to fahrenheit list

print(fahrenheit) # [68.7, 70.2, 70.5, 74.7, 66.0, 59.7, 59.0, 83.8, 85.3, 85.6, 92.1, 92.8, 91.2, 84.2, 71.96]

fahrenheit = [round(temperature * 1.8 + 32, 1) for temperature in temperatures] # list comprehension
print(fahrenheit) # [68.7, 70.2, 70.5, 74.7, 66.0, 59.7, 59.0, 83.8, 85.3, 85.6, 92.1, 92.8, 91.2, 84.2, 71.96]

primeNumbers = []
for i in range(2, 101): # loop through numbers 2 to 100
    isPrime = True
    for j in range(2, int(i**0.5) + 1): # check for factors from 2 to sqrt(i)
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbers.append(i)

print(primeNumbers) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]