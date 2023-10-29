# Write your solution
from datetime import datetime, timedelta

def calculate_total_average(screen_times):
    total = sum(sum(day) for day in screen_times)
    average = total / len(screen_times)
    return total, average

def main():
    filename = input("Filename: ")
    start_date_str = input("Starting date (dd.mm.yyyy): ")
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    num_days = int(input("How many days: "))

    screen_times = []
    for _ in range(num_days):
        input_line = input(f"Screen time {start_date_str}: ")
        day_screen_times = [int(x) for x in input_line.split()]
        screen_times.append(day_screen_times)
        start_date += timedelta(days=1)
        start_date_str = start_date.strftime("%d.%m.%Y")

    total, average = calculate_total_average(screen_times)

    with open(filename, "w") as file:
        file.write(f"Time period: {screen_times[0][0]}.{screen_times[0][1]}.{screen_times[0][2]}-{screen_times[-1][0]}.{screen_times[-1][1]}.{screen_times[-1][2]}\n")
        file.write(f"Total minutes: {total}\n")
        file.write(f"Average minutes: {average:.1f}\n")

        for i, day in enumerate(screen_times, 1):
            date_str = f"{day[0]}.{day[1]}.{day[2]}"
            file.write(f"{date_str}: {'/'.join(str(x) for x in day)}\n")

    print(f"Data stored in file {filename}")


if __name__ == "__main__":
    main()
