# tee ratkaisusi tänne
class CourseRecords:
    def __init__(self):
        self.courses = {}

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        
        if name not in self.courses:
            self.courses[name] = {"grade": grade, "credits": credits}
        else:
            if grade > self.courses[name]["grade"]:
                self.courses[name]["grade"] = grade

    def get_course_data(self, name):
        if name in self.courses:
            course_info = self.courses[name]
            return f"{name} ({course_info['credits']} cr) grade {course_info['grade']}"
        else:
            return "no entry for this course"

    def statistics(self):
        completed_courses = 0
        total_credits = 0
        grade_distribution = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}

        for course in self.courses.values():
            completed_courses += 1
            total_credits += course["credits"]
            grade_distribution[str(course["grade"])] += 1

        print(f"{completed_courses} completed courses, a total of {total_credits} credits")
        mean_grade = sum(course["grade"] for course in self.courses.values()) / completed_courses
        print(f"mean {mean_grade:.1f}")

        print("grade distribution")
        for grade, count in grade_distribution.items():
            print(f"{grade}: {'x' * count}")


records = CourseRecords()
print("1 add course")
print("2 get course data")
print("3 statistics")
print("0 exit")
print()
while True:
    command = input("command: ")
    
    if command == "1":
        records.add_course()
        print()
    elif command == "2":
        course_name = input("course: ")
        course_data = records.get_course_data(course_name)
        print(course_data)
        print()
    elif command == "3":
        records.statistics()
        print()
    elif command == "0":
        break
    else:
        print("Invalid command. Please try again.")
