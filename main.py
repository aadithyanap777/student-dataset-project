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