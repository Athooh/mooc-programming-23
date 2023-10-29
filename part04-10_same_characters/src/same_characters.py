# Write your solution here
def same_chars(word, idx1, idx2):
    if word[idx1] != word[idx2] or idx1 >= len(word) or idx2 >= len(word) or idx1 < 0 or idx2 < 0:
        return False
    else:
        return True
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 6))
    