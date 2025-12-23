
# Student Result System

students = []  # list 

while True:
    print("\nMenu")
    print("1. Add Student (Name,ID, Roll No, Marks)")
    print("2. Search Student by ID")
    print("3. Sort Students by Marks")
    print("4. Count Failed Students (Marks < 35)")
    print("5. Show Top 5 Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add student
    if choice == 1:
        student_id = input("Enter student ID: ")
        roll_no = input("Enter roll number: ")
        marks = float(input("Enter marks: "))
        students.append([student_id, roll_no, marks])
        print("Student added successfully")

    # 2. Search by ID
    elif choice == 2:
        search_id = input("Enter ID to search: ")
        found = False
        for s in students:
            if s[0] == search_id:
                print("Student Found:", s)
                found = True
                break
        if not found:
            print("Student not found")

    # 3. Sort by Marks (simple bubble sort)
    elif choice == 3:
        n = len(students)
        for i in range(n):
            for j in range(0, n-i-1):
                if students[j][2] < students[j+1][2]:  # compare marks
                    students[j], students[j+1] = students[j+1], students[j]
        print("Students sorted by marks:")
        for s in students:
            print(s)

    # 4. Count failed students
    elif choice == 4:
        fail_count = 0
        for s in students:
            if s[2] < 35:
                fail_count += 1
        print("Number of failed students:", fail_count)

    # 5. Show Top 5 students
    elif choice == 5:
        top5 = students[:5]  # after sorting, first 5
        print("Top 5 Students:")
        for s in top5:
            print(s)

    # 6. Exit
    elif choice == 6:
        print("Exiting program")
        break

    else:
        print("Invalid choice")