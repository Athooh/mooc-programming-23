# Write your solution here
def calculate_exercise_points(exercises_completed):
    return min(exercises_completed // 10, 10)

def calculate_grade(exam_points, exercise_points):
    total_points = exam_points + exercise_points
    if exam_points < 10:
        return 0  # Fail
    elif 15 <= total_points <= 17:
        return 1
    elif 18 <= total_points <= 20:
        return 2
    elif 21 <= total_points <= 23:
        return 3
    elif 24 <= total_points <= 27:
        return 4
    elif 28 <= total_points <= 30:
        return 5

if __name__ == "__main__":
    points_sum = 0
    pass_count = 0
    grade_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}

    while True:
        try:
            input_line = input("Exam points and exercises completed: ")
            if not input_line:
                break
            exam_points, exercises_completed = map(int, input_line.split())
            exercise_points = calculate_exercise_points(exercises_completed)
            grade = calculate_grade(exam_points, exercise_points)

            points_sum += exam_points + exercise_points
            if grade > 0:
                pass_count += 1
            grade_distribution[grade] += 1

        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

    print("Statistics:")
    total_students = sum(grade_distribution.values())
    points_average = points_sum / total_students
    pass_percentage = (pass_count / total_students) * 100

    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")

    print("Grade distribution:")
    for grade in range(5, -1, -1):
        stars = "*" * grade_distribution[grade]
        print(f"  {grade}: {stars}")



# def grade_statistics():
#     points = []
#     exercises = []
#     split_stat = []
    
#     stats = input("Exam points and exercises completed: ")
#     while stats != "" and len(stats) >= 3:
#         split_stat = stats.split(" ")
#         points.append(split_stat[0])
#         exercises.append(split_stat[1])       
#         stats = input("Exam points and exercises completed: ")
#     else:
#         print("Statistics:")
    
#     ex_points = []
#     for complete in exercises:
#         complete = (int(complete) / 100) * 100
        
#         if complete == 10:
#             points = 1
#             ex_points.append(points)
#         if complete == 20:
#             points = 2
#             ex_points.append(points)
#         if complete == 30:
#             points = 3
#             ex_points.append(points)
#         if complete == 40:
#             points = 4
#             ex_points.append(points)
#         if complete == 50:
#             points = 5
#             ex_points.append(points)
#         if complete == 60:
#             points = 6
#             ex_points.append(points)
#         if complete == 70:
#             points = 7
#             ex_points.append(points)
#         if complete == 80:
#             points = 8
#             ex_points.append(points)
#         if complete == 90:
#             points = 9
#             ex_points.append(points)
#         if complete == 100:
#             points = 10
#             ex_points.append(points)
            
    
#     print(points)
#     print(exercises)
#     print(ex_points)    
        
# grade_statistics()