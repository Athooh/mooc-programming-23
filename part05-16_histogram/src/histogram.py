# Write your solution here
def histogram(word):
    hist_dict = {}
    for char in word:
        hist_dict[char] = word.count(char)
        
    for k, v in hist_dict.items():
        print(f"{k} {v * '*'}")
if __name__ == '__main__':
    histogram("statistically")
