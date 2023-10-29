# Write your solution here
def add_student(database, name):
    database[name] = []

def add_course(database, name, course_data):
    course_name, grade = course_data

    if name in database:
        for idx, (course, existing_grade) in enumerate(database[name]):
            if course == course_name and existing_grade > 0:
                # If the course is already in the database and the existing grade is greater than 0,
                # we don't update the grade.
                return
        if grade > 0:
            database[name].append(course_data)
    else:
        print(f"{name}: no such person in the database")

def summary(database):
    num_students = len(database)
    most_courses_completed = 0
    best_average_grade = 0
    best_student = None

    for name, courses_completed in database.items():
        num_completed_courses = len([grade for _, grade in courses_completed if grade > 0])
        total_grade = sum(grade for _, grade in courses_completed if grade > 0)
        average_grade = total_grade / num_completed_courses if num_completed_courses > 0 else 0

        if num_completed_courses > most_courses_completed:
            most_courses_completed = num_completed_courses
            best_student = name

        if average_grade > best_average_grade:
            best_average_grade = average_grade
            best_student = name

    print(f"students {num_students}")
    print(f"most courses completed {most_courses_completed} {best_student}")
    print(f"best average grade {best_average_grade:.1f} {best_student}")

if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)


