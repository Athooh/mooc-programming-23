# Write your solution 
import csv

def store_personal_data(person: tuple):
    name, age, height = person

    with open('people.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([name, age, height])

if __name__ == '__main__':
    person_data = ("John Mason", 40, 190.5)
    store_personal_data(person_data)