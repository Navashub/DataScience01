my_courses = {
    'DataScience': [],
    'Software_engineering': [],
    'Digital_marketing': [],
    'Cyber_security': []
}

def addStudent():
    name_of_student = input("Enter the name of the student: ")
    print("Available courses:")
    for index, course in enumerate(my_courses):
        print(f"{index + 1}. {course}")
    
    courses_to_enroll = input("Enter the course numbers the student is taking (comma-separated): ")
    courses_to_enroll = courses_to_enroll.split(',')

    for course_number in courses_to_enroll:
        try:
            course_number = int(course_number.strip())
            if 1 <= course_number <= len(my_courses):
                selected_course = list(my_courses.keys())[course_number - 1]
                my_courses[selected_course].append(name_of_student)
            else:
                print(f"Invalid course number: {course_number}")
        except ValueError:
            print(f"Invalid input: {course_number}")


def viewCourses():
    for course, students in my_courses.items():
        print(f"{course}: {', '.join(students) if students else 'No students enrolled'}")

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. View Courses")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        addStudent()
    elif choice == '2':
        viewCourses()
    elif choice == '3':
        break
    else:
        print("Invalid choice, please try again.")
