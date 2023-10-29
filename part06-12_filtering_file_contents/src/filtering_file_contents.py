# Write your solution here
def filter_solutions():
    students = []
    with open("solutions.csv", "r") as solf:
        for line in solf:
            line = line.replace("\n", "").strip()
            students.append(line)
            
    print(students)
filter_solutions()