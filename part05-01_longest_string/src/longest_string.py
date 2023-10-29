# Write your solution here
def longest(strings: list):
    lng_wrd = max(len(wrd) for wrd in strings)
    
    for word in strings:
        if len(word) == lng_wrd:
            return word
        
if __name__ == '__main__':
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))