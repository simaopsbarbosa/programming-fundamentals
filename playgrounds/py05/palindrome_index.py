def palindrome_index(s): # returns int
    # check if palindrome
    if s == s[::-1]:
            return -1
    
    s = list(s)
    for i in range(len(s)):
        p = s.copy()
        p.pop(i)
        q = p.copy()
        q.reverse()
        if p == q:
            return i
    
    return -1

print(palindrome_index("aaab"))
    
    