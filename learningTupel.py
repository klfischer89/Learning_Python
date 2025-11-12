# student1 = ('John', 'Doe', 20, 'A') # Tuple representing a student
# student2 = ('Jane', 'Smith', 22, 'B') # Another student tuple

# student1 = ('John', 'Doe', 21, 'A-') # Updated age and grade for student1
# student1 = student1[:2] + (21, 'A+') # Correct way to update a tuple
# print(student1) # Output: ('John', 'Doe', 21, 'A+')

# student1_first_name = student1[0] # Accessing first name
# student1_last_name = student1[1] # Accessing last name

# print(f"Student: {student1_first_name} {student1_last_name}") # Output: Student: John Doe

# student1_first_name, student1_last_name, student1_age, student1_grade = student1 # Unpacking tuple
# print(f"Name: {student1_first_name}, Age: {student1_age}, Grade: {student1_grade}") # Output: Name: John, Age: 21, Grade: A+

d = ("Fuchs", [40, 50, 60, 70], ["Hase", "Igel"]) # Tuple with mixed data types
print(d) # Output: ('Fuchs', [40, 50, 60, 70], ['Hase', 'Igel'])
print(d[1][2]) # Accessing element from the list inside the tuple: Output: 60
print(d[2]) # Accessing the list of strings: Output: ['Hase', 'Igel']
print(d[0]) # Accessing the first element of the tuple: Output: Fuchs