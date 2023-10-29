# Write your solution here
import csv
from datetime import datetime

def final_points():
    start_times = {}
    with open('start_times.csv', 'r') as start_file:
        start_reader = csv.reader(start_file, delimiter=';')
        for row in start_reader:
            name, start_time_str = row
            start_time = datetime.strptime(start_time_str, '%H:%M')
            start_times[name] = start_time

    final_points_dict = {}
    with open('submissions.csv', 'r') as submissions_file:
        submissions_reader = csv.reader(submissions_file, delimiter=';')
        for row in submissions_reader:
            name, task, points, submit_time_str = row
            submit_time = datetime.strptime(submit_time_str, '%H:%M')
            start_time = start_times[name]
            time_difference = submit_time - start_time

            if 0 <= int(points) <= 6 and time_difference.total_seconds() <= 3 * 3600:
                if name not in final_points_dict:
                    final_points_dict[name] = {}

                task = int(task)
                points = int(points)
                if task not in final_points_dict[name] or points > final_points_dict[name][task]:
                    final_points_dict[name][task] = points

    for name, tasks in final_points_dict.items():
        total_points = sum(tasks.values())
        final_points_dict[name] = total_points

    return final_points_dict

if __name__ == '__main__':
    final_points_dict = final_points()
    print(final_points_dict)
