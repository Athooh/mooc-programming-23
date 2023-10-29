# Write your solution here
import csv
from datetime import datetime

def cheaters():
    start_times = {}
    with open('start_times.csv', 'r') as start_file:
        start_reader = csv.reader(start_file, delimiter=';')
        for row in start_reader:
            name, start_time_str = row
            start_time = datetime.strptime(start_time_str, '%H:%M')
            start_times[name] = start_time

    cheaters_list = []
    with open('submissions.csv', 'r') as submissions_file:
        submissions_reader = csv.reader(submissions_file, delimiter=';')
        for row in submissions_reader:
            name, task, points, submit_time_str = row
            submit_time = datetime.strptime(submit_time_str, '%H:%M')
            start_time = start_times[name]
            time_difference = submit_time - start_time
            if time_difference.total_seconds() > 3 * 3600:  
                if name not in cheaters_list:
                    cheaters_list.append(name)

    return cheaters_list

if __name__ == '__main__':
    cheaters_list = cheaters()
    print(cheaters_list)
