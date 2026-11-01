import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def create_dataset():
    data = {
        "StudentID": list(range(101, 121)),
        "Name": [
            "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", 
            "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan", 
            "Diya", "Sanya", "Ananya", "Aarohi", "Priya", 
            "Riya", "Neha", "Kavya", "Pooja", "Tanvi"
        ],
        "Age": [20, 21, 22, 20, 23, 21, 20, 22, 24, 21, 20, 22, 21, 23, 20, 21, 22, 20, 21, 22],
        "Course": [
            "Python", "SQL", "Mathematics", "English", "Python", 
            "SQL", "Mathematics", "English", "Python", "SQL", 
            "Mathematics", "English", "Python", "SQL", "Mathematics", 
            "English", "Python", "SQL", "Mathematics", "English"
        ],
        "Python": [85, 90, 78, 92, 88, 76, 95, 84, 89, 91, 80, 82, 87, 93, 79, 86, 88, 90, 85, 83],
        "SQL": [75, 88, 82, 90, 79, 85, 91, 84, 86, 89, 92, 78, 81, 87, 94, 80, 83, 86, 89, 91],
        "Mathematics": [80, 75, 91, 84, 89, 82, 86, 90, 78, 93, 85, 88, 92, 79, 87, 81, 90, 84, 86, 89],
        "English": [88, 92, 80, 85, 91, 79, 84, 87, 90, 82, 86, 94, 81, 85, 88, 90, 77, 83, 91, 86],
        "Attendance": [85, 90, 92, 88, 95, 80, 82, 89, 91, 94, 86, 87, 89, 90, 92, 85, 88, 90, 93, 84],
        "City": [
            "Mumbai", "Bangalore", "Delhi", "Hyderabad", "Chennai", 
            "Pune", "Mumbai", "Bangalore", "Delhi", "Hyderabad", 
            "Chennai", "Pune", "Mumbai", "Bangalore", "Delhi", 
            "Hyderabad", "Chennai", "Pune", "Mumbai", "Bangalore"
        ]
    }
    
    df = pd.DataFrame(data)
    return df
def display_students():
    df = create_dataset()
    print("=== All Student Records ===")
    print(df)
    return df
def dataset_info():
    df = create_dataset()
    print("=== Dataset Information ===")
    print("--- Head---")
    print(df.head())
    print("--- Tail ---")
    print(df.tail())
    print("--- Shape ---")
    print(df.shape)
    print("--- Columns ---")
    print(df.columns)
    print("--- Data Types ---")
    print(df.dtypes)

def select_students():
    df = create_dataset()
    student = df[["Name", "Python", "SQL", "Mathematics", "English"]]
    print("=== Selected Student Names & Subject Marks ===")
    print(student)
    return student
def filter_python_marks():
    df = create_dataset()
    filtered_marks = df[df["Python"] > 80]
    print("=== Students Scoring Above 80 in Python ===")
    print(filtered_marks)
    return filtered_marks
def filter_age():
    df = create_dataset()
    filtered_age = df[df["Age"] > 21]
    print("=== Students Aged Above 21 ===")
    print(filtered_age)
    return filtered_age
def filter_course():
    df = create_dataset()
    filtered_course = df[df["Course"] == "Python"]
    print("=== Students Enrolled in Python Course ===")
    print(filtered_course)
    return filtered_course

    