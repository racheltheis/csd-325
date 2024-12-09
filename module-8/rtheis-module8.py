#Rachel Theis
#CSD 325
#12.8.24

#This program will display the contents of a .json file, add a new item to the list, print the new list, and update the .json file 

import json
import os

class Student:
    def __init__(self, first_name, last_name, student_id, email):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.email = email

    def __str__(self):
        return f'{self.first_name} {self.last_name} : ID = {self.student_id} , Email = {self.email}'

def load_student_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    students = [
        Student(
            student['F_Name'],
            student['L_Name'],
            student['Student_ID'],
            student['Email']
        ) 
        for student in data
    ]
    return students

def print_student_list(students):
    print('Student List:')
    
    for student in students:
        print(student)

def add_student(students, first_name, last_name, student_id, email):
    new_student = Student(first_name, last_name, student_id, email)
    
    students.append(new_student)
    
    print(f'New student {first_name} {last_name} has been added to the list.')

def update_json_file(file_path, students):
    updated_data = [{
        'F_Name': student.first_name,
        'L_Name': student.last_name,
        'Student_ID': student.student_id,
        'Email': student.email
    } for student in students]
    
    with open(file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)
    
    print(f'\nThe {file_path} file has been updated with the new student data.')

def main():
    file_path = '/Users/Rachel/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Bellevue/Cohort/CSD 325/Assignments/module-8/student.json'
    
    if not os.path.exists(file_path):
        print(f'Error: The file at {file_path} does not exist.')
        return

    students = load_student_file(file_path)
    
    print_student_list(students)
    
    add_student(students, 'Rachel', 'Theis', 92897, 'rtheis@bellevue.edu')
    
    print('\nUpdated Student list:')
    print_student_list(students)
    
    update_json_file(file_path, students)

if __name__ == "__main__":
    main()
