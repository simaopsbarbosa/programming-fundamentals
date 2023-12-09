def discard_middle(s): # returns string, s is string
    if len(s) < 4:
        return ""
    return f"{s[0]}{s[1]}{s[-2]}{s[-1]}"
    