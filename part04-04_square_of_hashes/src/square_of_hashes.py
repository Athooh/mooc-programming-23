# Copy here code of line function from previous exercise
def line(times, char):
    if char != "":
        print(f"{char[0] * times}")
    else:
        print(f"{'*' * times}")

def square_of_hashes(size):
    # You should call function line here with proper parameters
    for x in range(size):
        line(size, "#")
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
