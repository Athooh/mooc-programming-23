# Write your solution here
def most_common_character(string):
    count_ch = [] 
    for i in string:
        chr = string.count(i)
        count_ch.append(chr)
    
    for i in string:
        if string.count(i) == max(count_ch):
            return i

if __name__ == '__main__':
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))