# Copy here code of line function from previous exercise
def line(times, char):
    if char != "":
        print(f"{char[0] * times}")
    else:
        print(f"{'*' * times}")

def triangle(size):
    # You should call function line here with proper parameters
    cnt = 0
    while cnt < size:
        cnt += 1
        line(cnt, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
