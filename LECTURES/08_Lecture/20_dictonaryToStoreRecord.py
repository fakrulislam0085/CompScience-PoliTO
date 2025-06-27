#creating dictionaries to store records of students
person1 = {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'GPA': 3.8}
person2 = {'name': 'Bob', 'age': 22, 'major': 'Mathematics', 'GPA': 3.6}
person3 = {'name': 'Charlie', 'age': 20, 'major': 'Physics', 'GPA': 3.9}

#creating a list of dictionaries
students = [person1, person2, person3]

#Access the first student's record
first_student = students[0]
print(first_student)
# Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'GPA': 3.8}

# Access the name of the second student
second_student_name = students[1]["name"]
print(second_student_name)  # Output: Bob

new_student = {'name': 'Diana', 'age': 23, 'major': 'Biology', 'GPA': 3.7}
students.append(new_student)
print(new_student)

# Update Charlie's GPA
students[2]['GPA'] = 4.0
print(students[2]['GPA'])

# Remove Bob's record
students = [student for student in students if student['name'] != 'Bob']
print(students)
