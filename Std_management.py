# -*- coding: utf-8 -*-
"""

@author: 
"""



students = []

def add_student(student_id,name,grade):
    for student in students :
        if student['ID'] == student_id:
            print(f" student with ID : {student_id} already exists !!!")
            return
    new_student = {
        'ID' : student_id,
        'Name' : name,
        'Grade' : grade
        }     
   
    students.append(new_student)
    print(f"Student: {name} added successfully !!!")    
    
    
add_student(101,"meg",'A')
add_student(102,"meghna",'B') 
add_student(103,"gogoi",'C')
add_student(102,"stbk",'D')   
