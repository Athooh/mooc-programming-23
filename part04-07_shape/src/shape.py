# Copy here code of line function from previous exercise and use it in your solution
def line(times, char):
    if char != "":
        print(f"{char[0] * times}")
    else:
        print(f"{'*' * times}")

# You can test your function by calling it within the following block
def shape(size1, ch1, size2, ch2):
    cnt = 0
    while size1 > cnt:
        cnt += 1
        line(cnt, ch1)
        
    for x in range(size2):
        line(cnt, ch2)

if __name__ == "__main__":
    shape(5, "x", 3, "*")