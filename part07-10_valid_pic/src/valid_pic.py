# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    def calculate_control_char(date_and_id: str) -> str:
        characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        nine_digit_number = int(date_and_id)
        remainder = nine_digit_number % 31
        return characters[remainder]

    if len(pic) != 11:
        return False

    date_and_id = pic[:6] + pic[-4:-1]  # Extract date of birth and personal identifier
    control_char = pic[-1]

    try:
        day = int(pic[:2])
        month = int(pic[2:4])
        year = int(pic[4:6])
        birth_date = datetime.strptime(f"{day:02d}-{month:02d}-{year:02d}", "%d-%m-%y")
    except ValueError:
        return False

    if birth_date.year % 4 != 0 and birth_date.month == 2 and birth_date.day == 29:
        return False

    century_marker = pic[6]
    if century_marker not in ['+', '-', 'A']:
        return False

    if calculate_control_char(date_and_id) != control_char:
        return False

    return True

# Test cases
print(is_it_valid("230827-906F"))  # Should print True
print(is_it_valid("120488+246L"))  # Should print True
print(is_it_valid("310823A9877"))  # Should print True
print(is_it_valid("290200-1239"))  # Should print False
