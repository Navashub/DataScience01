"""
Students - Big M, Dan, Timothy, Diana , Stacey, Ann
courses - Data Science, Software engineering, Digital marketing, Cyber security
--------------------------------------------------------------------------------

You are tasked with implementing a system to manage student enrollments in courses.
The list of couses available are: Data science, Software engineering, Digital Marketing & Cyber Security
The system should allow users to perform the following operations:

Students enrolling are: Big M, Dan, Timothy, Stacy, Anne, Diana
Diana is enrolled in 2 couses, Data science and Digital marketing

- Add a student to a course.
- Remove a student from a course.
- View all students enrolled in a particular course.
- View all courses a student is enrolled in.

Your task is to design and implement a Python program to fulfill these requirements.
You should use appropriate data structures to efficiently manage the student enrollments.
Additionally, ensure that the program can handle cases where a student may be enrolled in
multiple courses and where a course may have multiple students enrolled.

Your program should have a clear menu-driven interface, utilizing loops and conditional statements to guide
the user through the available options. Ensure that the program provides appropriate feedback to the user after each operation.

To further challenge yourself, consider implementing additional features such as error handling for invalid inputs and
ability to display statistics about course enrollments, such as the total number of students
enrolled in all courses or the number of courses each student is enrolled in.

"""

# DataScience = []
# Software_engineering = []
# Digital_marketing = []
# Cyber_security = []


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
    
    courses_enroll = input("Enter the course numbers the student is taking (for multiple seperate with commas): ")
    courses_enroll = courses_enroll.split(',')

    for course_number in courses_enroll:
        try:
            course_number = int(course_number.strip())
            if 1 <= course_number <= len(my_courses):
                selected_course = list(my_courses.keys())[course_number - 1]
                my_courses[selected_course].append(name_of_student)
            else:
                print(f"Invalid course number: {course_number}")
        except ValueError:
            print(f"Invalid input: {course_number}")

def removeStudent():
    name_of_student = input("Enter the name of the student to remove: ")

    for index, course in enumerate(my_courses):
        print(f"{index + 1}. {course}")

    selected_course_number = input("Enter the course number from which to remove the student: ")
    try:
        selected_course_number = int(selected_course_number.strip())

        if 1 <= selected_course_number <= len(my_courses):
            selected_course = list(my_courses.keys())[selected_course_number - 1]
            
            if name_of_student in my_courses[selected_course]:
                my_courses[selected_course].remove(name_of_student)

                print(f"{name_of_student} has been removed from {selected_course}")
            else:
                print(f"{name_of_student} is not in {selected_course}")
        else:
            print(f"invalid course selected {selected_course_number}")
    except ValueError:
        print(f"Invalid input: {selected_course_number}")



def viewCourses():
    for course, students in my_courses.items():
        print(f"{course}: {', '.join(students) if students else 'No students enrolled'}")

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. View Courses")
    print("3. Remove student")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        addStudent()
    elif choice == '2':
        viewCourses()
    elif choice == '3':
        removeStudent()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
