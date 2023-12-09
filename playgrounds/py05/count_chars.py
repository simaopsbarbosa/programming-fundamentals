import string

def count_chars(a_string): # returns a tuple (alphabetic , digits , symbols)
    letters = 0
    digits = 0
    symbols = 0
    
    for char in a_string:
        if char in string.ascii_letters:
            letters += 1
        elif char in string.digits:
            digits += 1
        else:
            symbols += 1
            
    return (letters, digits, symbols)

print(count_chars("hello1231 world!!"))