string = input("what is the string? ")
integer = int(input("what is the number of times you want to repeat the string? "))

new_string = "-".join([string] * integer)

print(new_string)