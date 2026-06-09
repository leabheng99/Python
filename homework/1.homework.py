# ==============================
# Student Management System
# ==============================

students = []


# Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    score = float(input("Enter Student Score: "))

    student = {
        "id": student_id,
        "name": name,
        "score": score
    }

    students.append(student)

    print("Student added successfully!\n")


# Display Students
def display_students():

    if len(students) == 0:
        print("No students found.\n")

    else:
        print("\n+--------------+----------------------+----------+")
        print("| ID           | Name                 | Score    |")
        print("+--------------+----------------------+----------+")

        for s in students:
            print(f"| {s['id']:<12} | {s['name']:<20} | {s['score']:<8} |")

        print("+--------------+----------------------+----------+\n")


# Delete Student
def delete_student():

    student_id = input("Enter Student ID to Delete: ")

    for s in students:

        if s["id"] == student_id:
            students.remove(s)

            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


# Update Student
def update_student():

    student_id = input("Enter Student ID to Update: ")

    for s in students:

        if s["id"] == student_id:

            s["name"] = input("Enter New Name: ")
            s["score"] = float(input("Enter New Score: "))

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


# Find Top Student
def find_top_student():

    if len(students) == 0:
        print("No students found.\n")
        return

    top_student = students[0]

    for s in students:

        if s["score"] > top_student["score"]:
            top_student = s

    print("\n========== Top Student ==========")

    print("+--------------+----------------------+----------+")
    print("| ID           | Name                 | Score    |")
    print("+--------------+----------------------+----------+")

    print(f"| {top_student['id']:<12} | {top_student['name']:<20} | {top_student['score']:<8} |")

    print("+--------------+----------------------+----------+\n")


# Main Menu
while True:

    print("========== Student Management System ==========")
    print("1. Add Student")
    print("2. List Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Find Top Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        add_student()

    # Display Students
    elif choice == "2":
        display_students()

    # Delete Student
    elif choice == "3":
        delete_student()

    # Update Student
    elif choice == "4":
        update_student()

    # Find Top Student
    elif choice == "5":
        find_top_student()

    # Exit Program
    elif choice == "6":
        print("Thankyou")
        break

    else:
        print("Invalid choice. Please try again.\n")
