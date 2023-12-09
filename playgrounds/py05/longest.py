def longest(s): # returns int
    s = s.split()
    max_len = 0
    for word in s:
        if len(word) > max_len:
            max_len = len(word)
            
    return max_len