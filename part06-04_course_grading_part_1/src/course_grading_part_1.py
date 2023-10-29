# write your solution here
students = {}
exercises = {}
records = {}

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

with open(student_info) as stdf:
    for line in stdf:
        line = line.replace("\n", "")
        row = line.split(";")
        if row[0] == "id":
            continue
        students[row[0]] = row[1] + " " + row[2]

with open(exercise_data) as exdf:
    for line in exdf:
        line = line.replace("\n", "")
        row = line.split(";")
        if row[0] == "id":
            continue
        exercises[row[0]] = row[1:]

for std_id, names in students.items():
    if std_id in exercises:
        ex_lst = exercises[std_id]
        tot = sum([int(x) for x in ex_lst])
        records[names] = tot

for k, v in records.items():
    print(f"{k} {v}")
