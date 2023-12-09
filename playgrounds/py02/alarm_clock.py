hours = int(input("hours? "))
min = int(input("minutes? "))

min = min + 6*60 + 51

if min >= 60:
    hours = hours + (min // 60)
    min = min % 60

if hours >= 24:
    hours = hours % 24

print("%02d:%02d" % (hours, min))
