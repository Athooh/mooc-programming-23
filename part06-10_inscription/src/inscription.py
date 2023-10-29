# Write your solution here
name = input("Whom should i sign this to: ").title()
file_doc = input("Where shall i save it: ")

with open(file_doc, 'w') as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team\n")