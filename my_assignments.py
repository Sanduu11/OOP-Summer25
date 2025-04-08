# 1. Variable assignment
my_number = 31576
my_string = "Hello, Python!"

# 2. Display variable types
print(type(my_number)) 
print(type(my_string))  

# 3. If statement
x = 15

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")

# 4. Create a list
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

# 5. For-loop through list
print("\nList of fruits:")
for fruit in fruits:
    print(fruit)

print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 6. Create a dictionary
student_dict = {
    "name": "Sandu",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

print(f"\nStudent name: {student_dict['name']}")
print(f"Student major: {student_dict['major']}")

# 7. Create a class
class Student:
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
    
    def get_info(self):
        return f"{self.name}, {self.age} years old, studying {self.major} with GPA {self.gpa}"
    
    def is_honors(self):
        return self.gpa >= 3.5

# Create instance
student_obj = Student("Bob", 21, "Mathematics", 3.9)

# Use methods
print("\nStudent information:")
print(student_obj.get_info())

if student_obj.is_honors():
    print("This student is on the honors list!")
else:
    print("This student is not on the honors list.")
