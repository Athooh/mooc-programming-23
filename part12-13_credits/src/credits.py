from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    total_credits = reduce(lambda x, y: x + y.credits, attempts, 0)
    return total_credits


def sum_of_passed_credits(attempts: list):
    passed_attempts = filter(lambda x: x.grade >= 1, attempts)
    
    total_credits = reduce(lambda x, y: x + y.credits, passed_attempts, 0)
    
    return total_credits

def average(attempts: list):
    passed_attempts = filter(lambda x: x.grade >= 1, attempts)

    total_grade = reduce(lambda x, y: x + y.grade, passed_attempts, 0)
    
    passed_count = len(list(filter(lambda x: x.grade >= 1, attempts)))

    if passed_count == 0:
        return 0
    return total_grade / passed_count

if __name__ == '__main__':
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)

    avg_grade = average([s1, s2, s3])
    print(avg_grade)