# students.py
students = [
    {"first_name": "Sandugash", "last_name": "Nurbolat", "index_number": "35176"},
    {"first_name": "Celina", "last_name": "Jones", "index_number": "354321"},
    {"first_name": "Bob", "last_name": "Brown", "index_number": "389012"}
]

for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
