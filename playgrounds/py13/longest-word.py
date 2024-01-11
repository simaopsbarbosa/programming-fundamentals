def longest(filename):
    file = open(filename, "r")
    longest_word = "a"
    for word in file.read().split():
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word