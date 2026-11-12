import csv
import random
from datetime import datetime

# Set seed so the data is reproducible (optional but professional)
random.seed(42)

departments = [
    "Computer Science",
    "Cybersecurity",
    "Software Engineering",
    "Information Technology",
    "Data Science",
    "Computer Engineering"
]

levels = [100, 200, 300, 400, 500]

def generate_student_id(index):
    return f"STU{2026}{index:04d}"

students = []

for i in range(1, 101):  # 100 students
    student_id = generate_student_id(i)
    department = random.choice(departments)
    level = random.choice(levels)
    
    # More realistic attendance (most students between 65–95%)
    attendance = round(random.uniform(58.0, 98.5), 1)
    
    # Average examination score (somewhat related to attendance)
    base_score = attendance * 0.7 + random.uniform(-15, 20)
    avg_score = round(max(35.0, min(98.0, base_score)), 1)
    
    students.append({
        "Student_ID": student_id,
        "Department": department,
        "Level": level,
        "Attendance_Percentage": attendance,
        "Average_Examination_Score": avg_score
    })

# Write the CSV file
with open("student_dataset.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Student_ID", "Department", "Level", "Attendance_Percentage", "Average_Examination_Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("✅ Dataset created successfully!")
print(f"Total students: {len(students)}")
print("File saved as: student_dataset.csv")