# Write your solution here
def line(times, char):
    if char != "":
        print(f"{char[0] * times}")
    else:
        print(f"{'*' * times}")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")