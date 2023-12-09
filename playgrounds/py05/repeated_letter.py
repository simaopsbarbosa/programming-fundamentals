def repeated_letter(s): # returns string (char)
    for char in s:
        if s.count(char) > 1:
            return char
    return None