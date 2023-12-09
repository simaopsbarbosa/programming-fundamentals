def map(pos, steps): # return tuple ( , )  
    return (pos[0] + steps.count("right") - steps.count("left") , pos[1] + steps.count("up")  - steps.count("down"))

print(map((0, 0), 'up-up-left-right-up-up'))