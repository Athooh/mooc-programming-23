# Write your solution here
def spruce(x):
    step = 2
    loop = 0
    cnt = 1
    cnt_lst = []
    while loop < x:
        # for y in range(1, x, step):
        loop += 1
        cnt_lst.append(cnt)
        cnt += step
    print("a spruce!")
    for y in cnt_lst:
        pos = max(cnt_lst) - y
        sp = pos / 2
        print(f"{' ' * int(sp)}{'*' * y}{' ' * int(sp)}")
    
    out_sp = int((max(cnt_lst)-1)/2)
    print(f"{' ' * out_sp}*{' ' * out_sp}")
            
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)