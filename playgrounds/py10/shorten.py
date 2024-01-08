def shorten(suffixes: list, base: int):
    def convert_value(num):
        if type(num) != str or not num.isdigit(): return str(num)
        for i, suffix in enumerate(suffixes[::-1]):
            exp = len(suffixes) - i - 1
            if int(num) // (base ** exp): return f"{str(int(num) // (base ** exp))} {suffix}"
    return convert_value